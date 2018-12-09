#!/usr/bin/env bash

#rpm -qa|grep sasl
#cyrus-sasl-plain-2.1.26-23.el7.x86_64
#cyrus-sasl-scram-2.1.26-23.el7.x86_64
#cyrus-sasl-lib-2.1.26-23.el7.x86_64
#cyrus-sasl-devel-2.1.26-23.el7.x86_64
#cyrus-sasl-gssapi-2.1.26-23.el7.x86_64
#cyrus-sasl-2.1.26-23.el7.x86_64
yum -y install cyrus-sasl-plain cyrus-sasl-scram cyrus-sasl-lib cyrus-sasl-devel cyrus-sasl-gssapi cyrus-sasl

cat >ca.info <<EOF
cn = libvirt.org
ca
cert_signing_key
EOF

servername=KVMServers
# (CN) field would contain the hostname of the server
# and would match the hostname used in the URI that clients pass to libvirt
# if clients will be connecting to the server using a URI of qemu://compute1.libvirt.org/system,
# so the CN must be "compute1.libvirt.org".
# If clients are likely to connect to the server by IP address,
# then one or more 'ip_address' fields should also be added.
cat > server.info <<EOF
organization = libvirt.org
cn = $servername
ip_address = 10.143.248.100
ip_address = 10.143.248.249
ip_address = 10.143.248.15
tls_www_server
encryption_key
signing_key
EOF

clientname=KVMClient
cat > client.info <<EOF
country = CN
state = Beijing
locality = Beijing
organization = libvirt.org
cn = $clientname
tls_www_client
encryption_key
signing_key
EOF

ips="10.143.248.100 10.143.248.15 10.143.248.249"
#/etc/pki/CA/cacert.pem on all clients and servers
certtool --generate-privkey > cakey.pem
certtool --generate-self-signed --load-privkey cakey.pem --template ca.info --outfile cacert.pem
for ip in $ips
do
    scp cacert.pem root@$ip:/etc/pki/CA/cacert.pem
done

# (CN) field would contain the hostname of the server and would match the hostname used in the URI that clients pass to libvirt
certtool --generate-privkey > serverkey.pem
certtool --generate-certificate --load-privkey serverkey.pem --load-ca-certificate cacert.pem --load-ca-privkey cakey.pem --template server.info --outfile servercert.pem
for ip in $ips
do
    cp serverkey.pem   /etc/pki/libvirt/private/
    cp servercert.pem /etc/pki/libvirt/
done

certtool --generate-privkey > clientkey.pem
certtool --generate-certificate --load-privkey clientkey.pem  --load-ca-certificate cacert.pem --load-ca-privkey cakey.pem --template client.info --outfile clientcert.pem
for ip in $ips
do
    cp clientkey.pem /etc/pki/libvirt/private/clientkey.pem
    cp clientcert.pem /etc/pki/libvirt/clientcert.pem
done

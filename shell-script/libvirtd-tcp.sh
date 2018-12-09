#!/usr/bin/env bash

/etc/krb5.conf
/var/kerberos/krb5kdc/kdc.conf


kdb5_util create -r KVM1 -s

#[root@KVM1 krb5.conf.d]# kadmin.local
#Authenticating as principal root/admin@KVM1 with password.
#kadmin.local:  add_principal libvirt/kvm1
#WARNING: no policy specified for libvirt/kvm1@KVM1; defaulting to no policy
#Enter password for principal "libvirt/kvm1@KVM1":
#Re-enter password for principal "libvirt/kvm1@KVM1":
#Principal "libvirt/kvm1@KVM1" created.
#kadmin.local:  ktadd -k /etc/libvirt/krb5.tab libvirt/kvm1
#Entry for principal libvirt/kvm1 with kvno 2, encryption type aes256-cts-hmac-sha1-96 added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type aes128-cts-hmac-sha1-96 added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type des3-cbc-sha1 added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type arcfour-hmac added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type camellia256-cts-cmac added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type camellia128-cts-cmac added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type des-hmac-sha1 added to keytab WRFILE:/etc/libvirt/krb5.tab.
#Entry for principal libvirt/kvm1 with kvno 2, encryption type des-cbc-md5 added to keytab WRFILE:/etc/libvirt/krb5.tab.
#kadmin.local:  quit

kadmin.local
add_principal libvirt/kvm1
ktadd -k /etc/libvirt/krb5.tab libvirt/kvm1

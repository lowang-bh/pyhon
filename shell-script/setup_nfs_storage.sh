#!/usr/bin/env bash

define_default_nfs_pool(){
cat >kvm-nfs-pool.xml <<EOF
<pool type='netfs'>
  <name>kvm-nfs-pool</name>
  <source>
    <host name='10.143.248.201'/>
    <dir path='/data/kvm'/>
    <format type='auto'/>
  </source>
  <target>
    <path>/mnt/kvm-nfs-storage</path>
    <permissions>
      <mode>0755</mode>
      <owner>0</owner>
      <group>0</group>
    </permissions>
  </target>
</pool>
EOF

mkdir -p /mnt/kvm-nfs-storage
virsh pool-define kvm-nfs-pool.xml
virsh pool-start kvm-nfs-pool
virsh pool-autostart kvm-nfs-pool
}

define_default_nfs_pool

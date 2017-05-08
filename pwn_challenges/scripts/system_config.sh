#!/bin/bash

# Restrict access to dmesg
if [ $(cat /proc/sys/kernel/dmesg_restrict) -ne 1 ]
then
	echo "kernel.dmesg_restrict=1" >> /etc/sysctl.conf
fi

# Turn off ASLR
if [ $(cat /proc/sys/kernel/randomize_va_space) -ne 0 ]
then
	echo "kernel.randomize_va_space=0" >> /etc/sysctl.conf
fi

# Restart to make the above settings live

# Hide processes. Adding this to /etc/fstab doesn't work in Ubuntu 12.04
# See https://bugs.launchpad.net/ubuntu/+source/mountall/+bug/1039887
mount -o remount,hidepid=2 /proc
chmod 1733 /tmp /var/tmp /dev/shm
cp limits.conf /etc/security/limits.d/ctf.conf

# Install Peda in the system
#cp -R /home/vagrant/peda /opt/peda
#mkdir /home/vagrant/priv_keys

#Install zip
#apt-get install zip,libc6-dev-i386
#apt-get install gdb

# Create & configure user accounts
filename="$1"
while read -r line
do
		echo "$line"
		read -a user_id <<< "$line"
    ./user_setup.sh "${user_id[0]}" "${user_id[1]}" "${user_id[2]}"
done < "$filename"

#zip -r priv.zip /home/vagrant/priv_keys

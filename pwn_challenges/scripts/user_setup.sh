#!/bin/bash

#exit on failure
set -e

if [ $(id -u) -ne 0 ]
then
    echo "Must be running as root"
    exit 1
fi

if [ $# -ne 3 ]
then
    echo "Usage: $0 ID Username Password"
    exit 1
fi

id=$1
username=$2
password=$3
home=/home/$username
admin_home=/home/`logname`

set_perms() {
    local ownergroup="$1"
    local perms="$2"
    local pn="$3"
    chown $ownergroup $pn
    chmod $perms $pn
}

del_user () {
    #chattr -a -i -R $home/
    #rm -rf $home
    userdel $username
    groupdel $username

}

create_user () {
    # create user, copy files from /home/cs628/skel
    #groupadd --gid $((10000+$id)) $username
    #useradd --uid $((10000+$id)) -g $username -k $admin_home/ctf1/home -m $username -p $password
    # disable password based login, probably not required if passwordless SSH login is disabled
    # passwd -l $username

    # prevent other users from reading contents of home directory
    # may need 770 if a challenge requires writing by the victim binary
    #set_perms $username:$username 750 $home

    # default login shell to /bin/bash
    #chsh -s /bin/bash $username

    #generate keys for SSH
    #mkdir -p $home/.ssh
    #ssh-keygen -N '' -f $home/.ssh/id_rsa
    #set_perms $username:$username 700  $home/.ssh
    #cp $home/.ssh/id_rsa.pub $home/.ssh/authorized_keys
    #cp $home/.ssh/id_rsa $admin_home/priv_keys/$username
    #set_perms $username:$username 640 $home/.ssh/authorized_keys
    #set_perms $username:$username 600 $home/.ssh/id_rsa
    #set_perms $username:$username 640 $home/.ssh/id_rsa.pub

    # eternal history file
    #touch $home/.bash_history
    #set_perms root:$username 660 $home/.bash_history
    # make append only
    #chattr +a $home/.bash_history
    # no limit on bash history file size
    #echo "export HISTFILESIZE=" >> $home/.bashrc
    #echo "export HISTSIZE=" >> $home/.bashrc

    # Log gdb history
    # PEDA must be installed on the system
    #echo "source /opt/peda/peda.py
    #set history save on
    #set history filename ~/.gdb_history
    #set history size 32768
    #set history expansion on" >> $home/.gdbinit

    # Mail user credentials on his/her IITK ID
    # Usage:
    # python send_mail.py <username> <list_of-attachments>
    # python $admin_home/ctf1/send_mail.py $username $home/.ssh/id_rsa $admin_home/ctf1/cs628-take-home.pdf $admin_home/ctf1/proxycommand.sh

	#Delete all users home folder content
	rm -rf $home/*
}

set_bin_flag_perms () {
# Usage
# set_bin_flag_perms <relative_path_to_binary>  <relative_path_to_flag> <uid_offset_for_problem_user> <flag_id>
# flag file doesn't exist yet

    binary="$1"
    flag_path="$2"
    uid_offset="$3"
    flag_id=$4
    binid=$(($uid_offset+$id))

    mkdir -p $home/$flag_id
    $admin_home/scripts/gen_flag.py "$flag_id" "$username" > "$home/$flag_path"
    cp $admin_home/challenges/$binary $home/$binary
    # setuid
    set_perms $binid:$username 4750 $home/$binary
    set_perms $binid:$binid  400 $home/$flag_path
    # make the flag and the binary immutable
    chattr +i $home/$binary
    chattr +i $home/$flag_path
}

add_question_from_dir () {
# Usage
# add_question_from_dir <question_id> <uid_offset_for_problem_user> <binary_name>
# This function will copy question folder content from $admin_home/ctf1/home/<question_id> to users home directory,
# generate a flag and set proper permissions to the copied files

    question_id="$1"
    uid_offset="$2"
    binary="$3"

    cp -r $admin_home/challenges/$question_id $home/
    set_bin_flag_perms $question_id/$binary $question_id/flag.txt $uid_offset $question_id
}


# del_user
# exit

 create_user

# Generate binaries and delete source codes if required
# cd $home
# cd $admin_home/challenges
# FLAG_T=`$admin_home/scripts/gen_flag.py 0 "$username"`
# make all
# rm Makefile
# rm $home/0/baby_steps.c

# Generate flags and set proper permissions to the binaries & flags
cd $admin_home/challenges
# add_question_from_dir 1 30000 1
#set_bin_flag_perms 1/drunk_coder 1/flag.txt 30000 1
# set_bin_flag_perms 2/el-ess 2/flag.txt 35000 2
# set_bin_flag_perms 3/feedback 3/flag.txt 40000 3
# set_bin_flag_perms 4/guess 4/flag.txt 45000 4
# set_bin_flag_perms 5/doge 5/flag.txt 50000 5

# Modify flag for question 5
# chattr -i $home/5/flag.txt
# python $admin_home/ctf1/whitespace.py `$admin_home/ctf1/gen_flag.py 5 $username` > $home/5/flag.txt
# chattr +i $home/5/flag.txt

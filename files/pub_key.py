#!/usr/bin/python3.2

import os
import re
import getpass
import paramiko
import datetime
from getpass import getpass


######### FONCTION DE
def deploy_key(key, server, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=username, password=password)
    client.exec_command('mkdir -p ~/.ssh/')
    client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % key)
    client.exec_command('chmod 644 ~/.ssh/authorized_keys')
    client.exec_command('chmod 700 ~/.ssh/')

def log_file(log):
    date = datetime.datetime.now()
    with open("/tmp/result_file.txt", "a+") as result:
       log_tmp = str(date) + "   " + log + "\n"
       result.write(str(log_tmp))
       print (log_tmp)
       

key = open(os.path.expanduser('~/.ssh/id_rsa.pub')).read()
print ("Saisir le mot de passe root des serveurs")
password = getpass()



with open("/etc/ansible/hosts", "r") as host:
     
     for ligne in host:
         liste = re.findall("^1",ligne)
         if liste:
           inventaire = (ligne.split()[0])
           with open("/tmp/inventaire.txt", "a+") as inventary:
                  hosts = inventary.write(inventaire+"\n")

           try:
             for ligne in liste:
                deploy_key(key, server=inventaire, username="root", password=password)
                log=inventaire + " Copie de la public key faite."
                log_file(log)
                       

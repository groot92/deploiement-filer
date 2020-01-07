#!/usr/bin/python 
# -*- coding: utf-8 -*-

DOCUMENTATION='''
module: user_ad
description: Module qui permet d'extraire le login d'AD
 
options:
  ad_name:
	description: nom de l'utilisateur AD
	required: yes
  ad_password:
	description: password de l'utilisateur
	required: yes
	
  ad_serveur:
	description: nom du serveur AD
	required: yes	

'''
	
	
import sys, os
import pprint

import ldap3
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE
from ldap3.core.exceptions import LDAPCursorError
from ansible.module_utils.basic import AnsibleModule  


def main():
    server_name = '10.0.1.2:389'
    domain_name = 'MYWORLDCOMPANY'
    user_name = 'automate'
    password = 'Password.'



#def main(): 
    module = AnsibleModule( 
        argument_spec = dict( 
            ad_name        = dict(required=True, type='str'), 
            ad_password    = dict(required=True, type='str', no_log=True), 
            ad_dc_name     = dict(required=True, type='str'),
            ad_serveur_ip  = dict(required=True, type='str'),
            
        )
    )      
#            users_path = ("/home/" + ad_dc_name + "/")        
        #argument_spec=dict(
        #module = AnsibleModule( 
    ad_name = module.params['ad_name']
    ad_password = module.params['ad_password']
    ad_dc_name = module.params['ad_dc_name']
    ad_serveur_ip = module.params['ad_serveur_ip']
    data = dict(
        output="La creation des homes est faite ",
    )
    users_path = ("/home/" + ad_dc_name + "/")

    try:
        def list_login (path,list):
             with open(users_path, "a+") as result_login:
                  result_login.write(str(list)+"\n")



        search_base = "cn=users, dc={ad_dc_name}, dc=net"
        server = Server(ad_serveur_ip, get_info=ALL)
        conn = Connection(server, user='{}\\{}'.format(ad_dc_name, ad_name), password=ad_password, authentication=NTLM, auto_bind=True)
        conn.search(search_base='cn=users,dc=MYWORLDCOMPANY,dc=net', search_filter='(objectclass=person)', attributes=[ALL_ATTRIBUTES])
        #conn.search(search_base, search_filter='(objectclass=person)', attributes=[ALL_ATTRIBUTES])

        for e in conn.entries:

            try:
               desc = e.description



            except LDAPCursorError:
                desc = ""
                user_list = str(e['sAMAccountName'])
                print (user_list)
#print(format_string.format(str(e.name), str(e.logonCount), str(e.lastLogon)[:19], str(e.accountExpires)[:19], desc))

                print(users_path)
                os.mkdir(users_path + user_list)
        #os.remove(users_path)
                #list_login(users_path, user_list)
                 
        module.exit_json(changed=True, success=data,msg=data)
    except Exception as ee:
        module.fail_json(msg='error')


if __name__  ==  '__main__':
    main()

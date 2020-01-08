# déploiement-filer
Le projet permet l’installation de serveurs de fichier sous CentOS ou Red Hat.

Dépendance
Serveur linux famille (Centos ou Red Hat)
La configuration réseau faite
Avoir un mot de passe root identique

Playbooks Ansible
- playbook deploiement des serveurs en workgroup
	- Installation des packages suivant la distribution
	- copie des fichiers de configuration
	- création du répertoire de partage
	- reboot des services samba

# Utilisation
Saisir la ligne suivante dans un terminal.
```console
$ ansible-playbook -i /etc/ansible/hosts /etc/ansible/playbook.yml
```
![image](https://drive.google.com/uc?export=view&id=1mL9pUiIQQLlZWGer43_AbsIygDjDzIgV)

Saisir le mot de passe "root" des serveurs.

L'installation est terminé
![image](https://drive.google.com/uc?export=view&id=17UP8F71K0V68pARHUWs1PQkv9yjDLExf)




# Variables
***Script: pub_key.py :***

| Variables  | Commantaires   |
| ------------ | ------------ |
|  deploy_key | Fonction qui utilise le module paramiko pour la connexion ssh aux serveurs  |
| log_file  |Fonction qui génère un fichier log dans /tmp/result_file.txt   |
| key  | Valeur de la public key  |
|  password |Mot de passe root   |
|  liste | pré-nettoyage du fichier host de Ansible ( garde uniquement les lignes qui débutent par "1"  |
|  inventaire | Liste les adresses ip de hosts Ansible  |


***playbook_ad* :**

| Variable  |Commantaires   |
| ------------ | ------------ |
| ad_name  | compte a privilège sur le DC "administrateur"  |
|   |   |

***Module: user_ad.py* :**

| Variable  |Commantaires   |
| ------------ | ------------ |
| Password_dc  | Mot de passe du compte a privilège sur le DC  |
|ad_password | Mot de passe du compte a privilège|
| ad_dc_name| nom du comtroleur de domaine|
|ad_serveur_ip | addresse IP du DC |
|users_path | chemin des Homes |
| server | information sur le DC |
| conn | Chaine de connexion au DC |
| user_list | login des utilisateurs |
|   |   |

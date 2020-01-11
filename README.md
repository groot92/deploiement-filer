# déploiement-filer
Le projet permet l’installation de serveurs de fichier sous CentOS ou Red Hat.

**Dépendances:**
Serveur linux famille (Centos ou Red Hat)
La configuration réseau faite
Avoir un mot de passe root identique

**Playbooks Ansible:**
- playbook deploiement des serveurs en workgroup :**playbook.yml**
	- Installation des packages suivant la distribution
	- copie des fichiers de configuration
	- création du répertoire de partage
	- reboot des services samba
	
- Playbook de configuration dans l'active directory :**playbook_ad.yml**
	- Installation des packages necessaire a l'AD suivant la distribution
	- Copie des fichiers de configuration
	- Ajout du serveur dans le domaine
	- creation des Home user via un module ansible
	
**Module Ansible: **
users_ad (Nom du module)
*arguments*:
ad_name (Nom du compte a privilège sur l'active directory)
ad_password (Mot de passe du compte)
ad_dc_name (Nom du controleur de domaine)
ad_serveur_ip (adresse IP du DC)

**Script Python:**
pub_key.py

Permet le deploiement de la cle publique ssh sur les serveurs.
# Utilisation
## Workgroup
Saisir la ligne suivante dans un terminal.
```console
$ ansible-playbook -i /etc/ansible/hosts /etc/ansible/playbook.yml
```
![image](https://drive.google.com/uc?export=view&id=1mL9pUiIQQLlZWGer43_AbsIygDjDzIgV)

Saisir le mot de passe "root" des serveurs.

L'installation est terminée
![image](https://drive.google.com/uc?export=view&id=17UP8F71K0V68pARHUWs1PQkv9yjDLExf)

### Active Directory
L' étape précédente doit imperativement etre faire avant l'integration à l'active directory.

Saisir dans un terminal :
```console
$ ansible-playbook -i /etc/ansible/hosts /etc/ansible/playbook_ad.yml
```
![image](https://drive.google.com/uc?export=view&id=18rTBbPdMNAVEM_VXoUB6uyMmKaG7xKAe)
Saisir le mot de passe du compte a privilège sur le DC.

L'installation est terminée
![image](https://drive.google.com/uc?export=view&id=1JUX5q2Jxkp9eptS0d8axwSnHUdDwryT3)

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
| password_dc  | Mot de passe du compte "administrateur" sur le DC  |
|user |Valeur "automate"|
|remote_host| lecture du host sur le serveur|
|remote_ip| @IP du serveur|
|dc-name| valeur "myworldcompany"
|ex_name| valeur "net"|
|dc_ip| @IP du DC|
|user_ad| Nom du module ansible pour la création des homes directory|

***Module: users_ad.py* :**

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


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

# Variables
***Script pub_key.py :***

| Variables  | Commantaires   |
| ------------ | ------------ |
|  deploy_key | Fonction qui utilise le module paramiko pour la connexion ssh aux serveurs  |
| log_file  |Fonction qui génère un fichier log dans /tmp/result_file.txt   |
| key  | Valeur de la public key  |
|  password |Mot de passe root   |
|  liste | pré-nettoyage du fichier host de Ansible ( garde uniquement les lignes qui débutent par "1"  |
|  inventaire | Liste les adresses ip de hosts Ansible  |




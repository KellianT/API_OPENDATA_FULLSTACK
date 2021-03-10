echo "Création du dossier .ssh s'il n'existe pas déjà"
ssh kellian@10.0.4.59 "mkdir .ssh"

echo "Copier la clé public du poste vers le serveur"
scp C:\\Users\utilisateur\.ssh\id_rsa.pub kellian@10.0.4.59:./.ssh/authorized_keys

echo "Désactive l'authentification par mot de passe du SSH"
ssh kellian@10.0.4.59 "sed 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config"

echo "Importe les fichiers app.py, fonctions.py et app.html"
scp  C:\Users\utilisateur\Desktop\Python\Projets\API_OPENDATA_FULLSTACK\BACK\app.py kellian@10.0.4.59:./app.py
scp  C:\Users\utilisateur\Desktop\Python\Projets\API_OPENDATA_FULLSTACK\BACK\fonctions.py kellian@10.0.4.59:./fonctions.py
scp -r C:\Users\utilisateur\Desktop\Python\Projets\API_OPENDATA_FULLSTACK\BACK\templates kellian@10.0.4.59:./
scp -r C:\Users\utilisateur\Desktop\Python\Projets\API_OPENDATA_FULLSTACK\BACK\static kellian@10.0.4.59:./




clear


echo "Déployer script.sh"
scp  C:\Users\utilisateur\Desktop\Python\Projets\API_OPENDATA_FULLSTACK\SCRIPTS\scripts.sh kellian@10.0.4.59:./script.sh

echo "Ouvrir les droits du script"
ssh kellian@10.0.4.59 "chmod 777 ./script.sh"

echo "Executer le script"
ssh -t kellian@10.0.4.59 "sudo -S ./script.sh"

clear

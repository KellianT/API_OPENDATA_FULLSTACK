__Guide d'utilisation :__

Télécharger repo Git # API_OPENDATA_FULLSTACK

Déployez le script .bat (Qui va déplyer le script et set up la VM) à la fin de l'execution du scrip il va run le serveur HTTP.

Il faudra se rendre à l'adresse du serveur dans HOME '10.0.4.59:80', 

Il y aura a faire la recherche de la station, ou toutes les stations sont sur la page.











__Dossier HTML :__ Documentation de l' API et du fichier fonction



__Dossier BACK composé de :__


__Dans Test BACK :__

- init.py : Le fichier qui sert à importer les modules

- csv_test.csv : Une copie minimaliste du CSV téléchargé (TAM) afin de réaliser les tests

- tests_back.py : Test unitaires des fonctions



__Dans static :__


- CSS : Partie esthétique de la réponse

- JS : Dynamise les réponses des requêtes


__Dans templates :__


- TAM_MMM_TpsReel.csv : fichier CSV de la TAM

- init.py : Le fichier qui sert à importer les modules

- fonctions.py : Les fonctions liées à l' API

- test_api.py : Les tests de l' API


__Dans dossier Script se trouvent les dossier d'installation :__ 


- script_install.bat : Set up les clefs SSh pour un accès simplifié, Il importe le fichier back sur le serveur, déploie et execute script.

- scripts.sh : Installe l'environnement de travail qu'il utilise et installe les modules nécéssaire (Flask, Flask CORS, Télécharge/installe MAJ et éxecute le serveur).

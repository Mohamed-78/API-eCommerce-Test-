#Utiliser une image pyhton
FROM python:3.10

#Le repertoire de travail
WORKDIR /app

#Fichier du projet django dans le conteneur
COPY . /app/

#Installer les dependences
RUN pip install -r requirements.txt

#Le port de l'application
EXPOSE 8000

#Commande pour demarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
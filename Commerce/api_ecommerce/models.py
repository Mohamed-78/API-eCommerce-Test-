import bcrypt
from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=225)
    slug = models.CharField()

    def __str__(self):
        return f"{self.libelle}"


class SousCategorie(models.Model):
    libelle = models.CharField(max_length=225)
    categorie_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    slug = models.CharField()

    def __str__(self):
        return f"{self.libelle} - {self.categorie_id}"


class Produit(models.Model):
    nom = models.CharField(max_length=225)
    description = models.TextField()
    prix = models.IntegerField()
    cover = models.ImageField(upload_to='cover/')
    slug = models.CharField(max_length=225)
    photos = models.ImageField(upload_to='photos/')
    sous_categorie_id = models.ForeignKey(SousCategorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=225)
    prenoms = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    ville = models.CharField(max_length=225)
    commune = models.CharField(max_length=225)
    mot_de_passe = models.CharField(max_length=225)

    def check_password(self, mot_de_passe):
        # Vérifiez le mot de passe en utilisant bcrypt
        return check_password(mot_de_passe, self.mot_de_passe)


class Commentaire(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commentaire = models.TextField()


class Favoris(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)
    slug = models.CharField(max_length=225)


class Message(models.Model):
    titre = models.CharField(max_length=225)
    message = models.TextField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

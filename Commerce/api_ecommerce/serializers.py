from rest_framework import serializers
from .models import Client
from .models import Message, Commentaire, Favoris, Produit

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nom', 'prenoms', 'contact', 'ville', 'commune', 'mot_de_passe']

class MessageClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'titre', 'message', 'client_id']

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'commentaire', 'client_id', 'produit_id']

class FavoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = ['id', 'slug', 'client_id', 'produit_id']

class ConnexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['contact','mot_de_passe']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
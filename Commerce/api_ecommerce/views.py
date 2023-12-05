from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from .serializers import ClientSerializer, CommentaireSerializer, FavoriSerializer, ConnexionSerializer, ProduitSerializer
from .serializers import MessageClientSerializer
from .models import Client, Produit, Favoris
from .models import Message
from .function import check_existance, token_client
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


@api_view(['POST'])
def InscriptionClient(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            mot_de_passe_brute = request.data['mot_de_passe']
            mot_de_passe_hashe = make_password(mot_de_passe_brute)

            # Vérifiez si un contact existe
            existing_contact = Client.objects.filter(contact=request.data['contact']).first()

            if existing_contact:
                return Response({'error_message': 'Ce contact existe deja'}, status=status.HTTP_400_BAD_REQUEST)

            client = Client.objects.create(
                nom=request.data['nom'],
                prenoms=request.data['prenoms'],
                contact=request.data['contact'],
                ville=request.data['ville'],
                commune=request.data['commune'],
                mot_de_passe= mot_de_passe_hashe
            )

            # token, created = Token.objects.get_or_create(client=Client)
            # return Response({'token': token.key, 'client_id': client.id}, status=status.HTTP_201_CREATED)
            return Response(ClientSerializer(client).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def ConnexionClient(request):
    if request.method == 'POST':
        serializer = ConnexionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            contact = serializer.validated_data['contact']
            mot_de_passe = serializer.validated_data['mot_de_passe']

            client = Client.objects.get(contact=contact)
            if client.check_password(mot_de_passe):
                return Response({
                    'token': token_client(client),
                    'infos': data,
                    'status': 'success'
                })
            else:
                return Response({'message': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NouveauMessageView(APIView):
    def post(self, request, client_id):
        #verifier si le client existe
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({"client": ["Le client n'existe pas"]}, status=status.HTTP_400_BAD_REQUEST)

        #Crer l'objet Message en utilisant le client_id
        serializer = MessageClientSerializer(data={
            "titre": request.data.get("titre"),
            "message": request.data.get("message"),
            "client_id": client_id
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NouveauCommentaireView(APIView):
    def post(self, request, client_id, produit_id):
        #verifier si le client_id ou le produit_id n'existe pas

        client, client_error = check_existance(Client, client_id, "client_id")
        if client_error:
            return Response({"client": ["Le client n'existe pas"]}, status=status.HTTP_400_BAD_REQUEST)

        produit, produit_error = check_existance(Produit, produit_id, "produit_id")
        if produit_error:
            return Response({"Produit": ["Le produit n'existe pas"]}, status=status.HTTP_400_BAD_REQUEST)

        #Recuperer donnees du formulaire
        serializer = CommentaireSerializer(data={
            "commentaire":request.data.get("commentaire"),
            "client_id": client_id,
            "produit_id": produit_id
        })

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Message enregistré avec succès!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NouveauFavoriView(APIView):
    def post(self, request, client_id, produit_id):
        #verifier si le client_id ou le produit_id n'existe pas

        client, client_error = check_existance(Client, client_id, "client_id")
        if client_error:
            return Response({"client": ["Le client n'existe pas"]}, status=status.HTTP_400_BAD_REQUEST)

        produit, produit_error = check_existance(Produit, produit_id, "produit_id")
        if produit_error:
            return Response({"Produit": ["Le produit n'existe pas"]}, status=status.HTTP_400_BAD_REQUEST)

        #Verifier si le client a deja ajouter le produit comme favori
        favori_existe = Favoris.objects.filter(client_id=client_id, produit_id=produit_id).exists()
        if favori_existe:
            return Response({"message": ["Ce produit a déjà été ajouté comme favori par ce client"]}, status=status.HTTP_400_BAD_REQUEST)

        #Recuperer donnees du formulaire
        serializer = FavoriSerializer(data={
            "slug": request.data.get("slug"),
            "client_id": client_id,
            "produit_id": produit_id
        })

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Favori enregistré avec succès!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListeProduitView(APIView):
    def get(self, request, produit_id=None):
        if produit_id:
            # Si product_id est fourni, récupérez un produit spécifique
            produit = self.get_product(produit_id)
            serializer = ProduitSerializer(produit)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Sinon, récupérez la liste complète des produits
            produits = Produit.objects.all()
            serializer = ProduitSerializer(produits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_product(self, product_id):
        try:
            return Produit.objects.get(pk=product_id)
        except Produit.DoesNotExist:
            raise Http404

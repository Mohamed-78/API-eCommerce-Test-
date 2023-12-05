from django.contrib import admin
from django.urls import path

from api_ecommerce.views import InscriptionClient
from api_ecommerce.views import NouveauMessageView
from api_ecommerce.views import NouveauCommentaireView
from api_ecommerce.views import NouveauFavoriView
from api_ecommerce.views import ConnexionClient
from api_ecommerce.views import ListeProduitView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inscription', InscriptionClient, name='inscription.client'),
    path('api/nouveau-message-client/<int:client_id>', NouveauMessageView.as_view(), name='nouveau-message-client'),
    path('api/nouveau-commentaire-client/<int:client_id>/<int:produit_id>', NouveauCommentaireView.as_view(), name='nouveau-commentaire-client'),
    path('api/nouveau-favori-client/<int:client_id>/<int:produit_id>', NouveauFavoriView.as_view(), name='nouveau-favori-client'),
    path('api/connexion', ConnexionClient, name='connexion-client'),
    path('api/produits', ListeProduitView.as_view(), name='liste-produit'),
    path('api/produits/<int:produit_id>', ListeProduitView.as_view(), name='details-produit')
]

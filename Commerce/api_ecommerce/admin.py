from django.contrib import admin
from .models import Produit
from .models import Categorie
from .models import SousCategorie
# Register your models here.

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    afficher_produit = ('nom', 'prix', 'sous_categorie_id', 'cover')

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    afficher_categorie = ('libelle', 'slug')

@admin.register(SousCategorie)
class SousCategorieAdmib(admin.ModelAdmin):
    afficher_sous_categorie = ('libelle', 'categorie_id', 'slug')
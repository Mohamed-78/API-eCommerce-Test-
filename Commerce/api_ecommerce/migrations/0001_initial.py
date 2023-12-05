# Generated by Django 4.2.6 on 2023-10-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=225)),
                ('slug', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('prenoms', models.CharField(max_length=225)),
                ('contact', models.CharField(max_length=225)),
                ('ville', models.CharField(max_length=225)),
                ('commune', models.CharField(max_length=225)),
                ('mot_de_passe', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=225)),
                ('slug', models.CharField()),
                ('categorie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('prix', models.IntegerField()),
                ('cover', models.ImageField(upload_to='cover/')),
                ('slug', models.CharField(max_length=225)),
                ('photos', models.ImageField(upload_to='photos/')),
                ('sous_categorie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.souscategorie')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=225)),
                ('message', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.client')),
            ],
        ),
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=225)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.client')),
                ('produit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.client')),
                ('produit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_ecommerce.produit')),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-24 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Maison', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=0, max_length=40)),
                ('mail', models.CharField(default=0, max_length=40)),
                ('message', models.CharField(default=0, max_length=400)),
                ('client', models.CharField(default=0, max_length=40)),
                ('propriete_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Maison.propriete')),
            ],
        ),
    ]

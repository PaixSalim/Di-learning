# Generated by Django 4.1.3 on 2023-01-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0003_chambre_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='photo',
            field=models.ImageField(default='img_chambre/default.jpg', upload_to='img_chambre', verbose_name='photo de chambre'),
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_alter_chambre_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chambre',
            name='date_creation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='chambre',
            name='photo',
            field=models.ImageField(default='0', upload_to='img_chambre', verbose_name='photo de chambre'),
        ),
    ]

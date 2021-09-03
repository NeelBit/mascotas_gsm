# Generated by Django 3.2.5 on 2021-08-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='medida',
            field=models.CharField(choices=[('chico', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande'), ('otro', 'No se')], default='otro', help_text='Seleccione el tamaño que cree mas adecuado.', max_length=15),
        ),
    ]
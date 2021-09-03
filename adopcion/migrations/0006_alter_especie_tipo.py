# Generated by Django 3.2.5 on 2021-08-19 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0005_alter_especie_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especie',
            name='tipo',
            field=models.CharField(choices=[('perro', 'Perro'), ('gato', 'Gato'), ('otro', 'Otro')], default='otro', help_text='Seleccione la especie.', max_length=10, null=True),
        ),
    ]

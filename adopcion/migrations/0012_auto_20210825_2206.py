# Generated by Django 3.2.5 on 2021-08-26 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0011_auto_20210825_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imgI',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imgII',
            new_name='img2',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imgIII',
            new_name='img3',
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-03 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contato'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'verbose_name': 'Contato', 'verbose_name_plural': '2. Contatos'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': '1. Usuários'},
        ),
    ]

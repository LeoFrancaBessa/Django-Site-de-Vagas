# Generated by Django 3.2.2 on 2021-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210608_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='data_cadastro',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
    ]
# Generated by Django 3.2.2 on 2021-06-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_vacanciesapplications'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacanciesapplications',
            name='data',
            field=models.DateTimeField(auto_now=True, verbose_name='Data do Registro'),
        ),
    ]

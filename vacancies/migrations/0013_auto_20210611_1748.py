# Generated by Django 3.2.2 on 2021-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0012_alter_vacancies_data_criacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacanciesapplications',
            name='data_inscricao',
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='data_criacao',
            field=models.DateField(auto_now=True),
        ),
    ]

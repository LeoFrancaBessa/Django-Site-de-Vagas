# Generated by Django 3.2.2 on 2021-06-11 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_auto_20210611_0836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacanciesapplications',
            old_name='data',
            new_name='data_inscricao',
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-19 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0004_vacancy_cat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0002_remove_vacancy_cat_alter_vacancy_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.CharField(max_length=256),
        ),
    ]

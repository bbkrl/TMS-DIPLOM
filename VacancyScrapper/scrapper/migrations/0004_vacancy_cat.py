# Generated by Django 4.1.1 on 2022-09-18 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0003_alter_vacancy_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scrapper.jobcategory'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.8 on 2022-10-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_info_city_info_country_info_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]

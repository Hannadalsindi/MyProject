# Generated by Django 4.0.8 on 2022-10-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_alter_info_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='id',
            field=models.AutoField(max_length=10, primary_key=True, serialize=False),
        ),
    ]

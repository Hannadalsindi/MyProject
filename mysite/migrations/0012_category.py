# Generated by Django 4.0.8 on 2022-10-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_alter_info_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]

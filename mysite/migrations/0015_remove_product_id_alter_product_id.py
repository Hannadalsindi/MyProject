# Generated by Django 4.0.8 on 2022-10-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ID',
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]

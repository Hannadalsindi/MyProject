# Generated by Django 4.0.8 on 2022-10-19 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0048_rename_category_pro_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pro',
            old_name='category_id',
            new_name='Category_id',
        ),
    ]

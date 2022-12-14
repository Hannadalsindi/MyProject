# Generated by Django 4.0.8 on 2022-10-11 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0017_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(blank=True, max_length=30)),
                ('Sku', models.CharField(max_length=30, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='')),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.category')),
            ],
        ),
    ]

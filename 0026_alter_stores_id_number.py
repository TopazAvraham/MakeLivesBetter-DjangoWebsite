# Generated by Django 4.1 on 2022-09-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_stores_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='id_number',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]
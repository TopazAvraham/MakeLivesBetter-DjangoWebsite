# Generated by Django 4.1 on 2022-08-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
# Generated by Django 4.1 on 2022-09-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_feature_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='details',
            field=models.CharField(max_length=400),
        ),
    ]
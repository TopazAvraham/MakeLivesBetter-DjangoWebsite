# Generated by Django 4.1 on 2022-09-02 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_stores_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

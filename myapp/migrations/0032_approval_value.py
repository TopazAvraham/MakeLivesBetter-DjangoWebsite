# Generated by Django 4.1 on 2022-09-06 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_alter_approval_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='value',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
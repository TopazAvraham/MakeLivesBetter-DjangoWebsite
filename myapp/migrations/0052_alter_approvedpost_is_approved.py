# Generated by Django 4.1 on 2022-09-07 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_alter_approvedpost_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedpost',
            name='is_approved',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-09 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0057_alter_volunteeringoption_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='id_number',
        ),
    ]
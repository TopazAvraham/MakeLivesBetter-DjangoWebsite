# Generated by Django 4.1 on 2022-08-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]

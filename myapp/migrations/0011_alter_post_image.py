# Generated by Django 4.1 on 2022-08-28 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='defultl.jpg', upload_to='files/'),
        ),
    ]

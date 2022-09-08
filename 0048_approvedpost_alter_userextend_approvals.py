# Generated by Django 4.1 on 2022-09-06 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_rename_post_userextend_approvals'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='files/')),
                ('is_approved', models.BooleanField()),
                ('value', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='userextend',
            name='approvals',
            field=models.ManyToManyField(to='myapp.approvedpost'),
        ),
    ]
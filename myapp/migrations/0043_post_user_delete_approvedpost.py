# Generated by Django 4.1 on 2022-09-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_approvedpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.userextend'),
        ),
        migrations.DeleteModel(
            name='ApprovedPost',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-03 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dete_posted',
            new_name='date_posted',
        ),
    ]

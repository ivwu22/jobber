# Generated by Django 3.1.7 on 2021-03-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210316_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='category',
        ),
    ]
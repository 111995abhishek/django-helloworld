# Generated by Django 2.2.6 on 2019-10-11 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20191011_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISDN',
            new_name='Isbn',
        ),
    ]

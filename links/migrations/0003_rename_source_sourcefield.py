# Generated by Django 4.0.3 on 2022-07-15 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_remove_link_category_link_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Source',
            new_name='SourceField',
        ),
    ]
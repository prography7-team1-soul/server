# Generated by Django 4.0.4 on 2022-07-22 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_alter_club_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['name']},
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-22 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_club_detail_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ('name',)},
        ),
    ]
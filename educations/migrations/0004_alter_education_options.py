# Generated by Django 4.0.4 on 2022-07-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0003_education_detail_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['name']},
        ),
    ]

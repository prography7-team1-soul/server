# Generated by Django 4.0.3 on 2022-07-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_link_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

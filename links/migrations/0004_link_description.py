# Generated by Django 4.0.3 on 2022-07-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_rename_source_sourcefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-07-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
        ('accounts', '0004_alter_user_fcm_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='link_bookmarks',
            field=models.ManyToManyField(blank=True, to='links.link'),
        ),
    ]

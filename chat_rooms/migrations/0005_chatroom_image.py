# Generated by Django 4.0.4 on 2022-07-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_rooms', '0004_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(default='', upload_to='chat_room'),
            preserve_default=False,
        ),
    ]
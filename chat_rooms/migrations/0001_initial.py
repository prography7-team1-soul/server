# Generated by Django 4.0.4 on 2022-07-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('개발자', 'Developer'), ('기획자', 'Productmanger'), ('디자이너', 'Designer')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31)),
                ('url', models.URLField()),
                ('has_password', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(to='chat_rooms.category')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educations', '0002_sns_image_alter_education_education_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='detail_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]

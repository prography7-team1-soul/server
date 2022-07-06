# Generated by Django 4.0.4 on 2022-07-06 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0004_alter_club_club_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('image', models.ImageField(upload_to='club')),
                ('description', models.TextField()),
                ('recruitment_personnel', models.PositiveIntegerField()),
                ('recruitment_at', models.CharField(max_length=31)),
                ('education_description', models.TextField()),
                ('education_cost', models.PositiveIntegerField()),
                ('education_area', models.CharField(max_length=31)),
                ('education_period', models.CharField(max_length=31)),
                ('home_url', models.URLField()),
                ('recruitment_fields', models.ManyToManyField(to='club.recruitmentfield')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitmentField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('개발자', 'Developer'), ('기획자', 'Productmanger'), ('디자이너', 'Designer')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SNS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educations.education')),
            ],
        ),
    ]

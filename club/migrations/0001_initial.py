# Generated by Django 4.0.4 on 2022-07-07 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('image', models.ImageField(upload_to='club')),
                ('club_description', models.TextField()),
                ('recruitment_personnel', models.PositiveIntegerField()),
                ('recruitment_at', models.CharField(max_length=31)),
                ('activity_description', models.TextField()),
                ('activity_cost', models.PositiveIntegerField()),
                ('activity_area', models.CharField(max_length=31)),
                ('activity_period', models.CharField(max_length=31)),
                ('home_url', models.URLField()),
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
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='recruitment_fields',
            field=models.ManyToManyField(to='club.recruitmentfield'),
        ),
    ]

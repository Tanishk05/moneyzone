# Generated by Django 4.2.6 on 2023-11-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('facebook', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]

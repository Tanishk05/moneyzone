# Generated by Django 4.2.6 on 2023-10-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('items', models.TextField()),
                ('image', models.ImageField(upload_to='static/images/package')),
                ('description', models.TextField()),
            ],
        ),
    ]

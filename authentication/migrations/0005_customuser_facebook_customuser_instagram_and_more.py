# Generated by Django 4.2.6 on 2023-11-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='facebook',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='instagram',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

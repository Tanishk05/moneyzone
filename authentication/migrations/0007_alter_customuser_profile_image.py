# Generated by Django 4.2.6 on 2023-11-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_customuser_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_image",
            field=models.ImageField(null=True, upload_to="images/profile_images"),
        ),
    ]

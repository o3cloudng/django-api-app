# Generated by Django 4.1.2 on 2022-10-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0016_alter_user_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_image//%Y/%m/%d"
            ),
        ),
    ]

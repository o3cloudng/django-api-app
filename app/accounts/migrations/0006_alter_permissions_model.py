# Generated by Django 4.1.1 on 2022-09-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_role_permissions_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permissions",
            name="model",
            field=models.CharField(
                choices=[("User", "User"), ("Role", "Role")], max_length=500
            ),
        ),
    ]

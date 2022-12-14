# Generated by Django 4.1.1 on 2022-09-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_rename_permissions_permission"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permission",
            name="model",
            field=models.CharField(
                choices=[
                    ("GENERAL", "General"),
                    ("UserModule", "Usermodule"),
                    ("RoleModule", "Rolemodule"),
                ],
                default="GENERAL",
                max_length=500,
            ),
        ),
    ]

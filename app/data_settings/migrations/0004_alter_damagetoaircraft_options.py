# Generated by Django 4.1.1 on 2022-09-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_settings", "0003_damagetoaircraft"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="damagetoaircraft",
            options={
                "ordering": ["-created_at"],
                "permissions": [("export_data_settings", "can export data settings")],
            },
        ),
    ]

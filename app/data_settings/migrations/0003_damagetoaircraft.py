# Generated by Django 4.1.1 on 2022-09-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_settings", "0002_rename_states_state"),
    ]

    operations = [
        migrations.CreateModel(
            name="DamageToAirCraft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=500, unique=True)),
                ("description", models.CharField(max_length=1500)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]

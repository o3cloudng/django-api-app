# Generated by Django 4.1.2 on 2022-10-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aircraft_template_manager", "0006_alter_aircrafttemplatemanager_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    ["deactivate_manufacturer", "can deactivate aircraft manufacturer"],
                    ["print_manufacturer", "can print aircraft manufacturer"],
                    ["import_manufacturer", "can import aircraft manufacturer"],
                    ["export_manufacturer", "can export aircraft manufacturer"],
                ],
            },
        ),
        migrations.RemoveField(
            model_name="aircrafttemplatemanager",
            name="manufacturer_company_full_name",
        ),
        migrations.RemoveField(
            model_name="aircrafttemplatemanager",
            name="manufacturer_company_name",
        ),
    ]
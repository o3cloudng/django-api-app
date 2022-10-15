# Generated by Django 4.1.1 on 2022-10-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AircraftTemplateManager",
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
                ("manufacturer_company_name", models.CharField(max_length=500)),
                ("manufacturer_company_full_name", models.CharField(max_length=500)),
                ("icao_code", models.CharField(max_length=500)),
                ("aircraft_model", models.CharField(max_length=500)),
                ("year_manufactured", models.DateField(max_length=500)),
                ("model_3d_image", models.ImageField(upload_to="model_3d_image")),
                ("type", models.CharField(max_length=1500)),
                ("description", models.CharField(max_length=500)),
                ("engine_type", models.CharField(max_length=500)),
                ("engine_count", models.CharField(max_length=500)),
                ("wtc", models.CharField(max_length=500)),
                ("iata", models.CharField(max_length=500)),
            ],
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    [
                        "deactivate_aircraft_template_manager",
                        "can deactivate aircraft template manager",
                    ],
                    [
                        "print_aircraft_template_manager",
                        "can print aircraft template manager",
                    ],
                    [
                        "import_aircraft_template_manager",
                        "can import aircraft template manager",
                    ],
                    [
                        "export_aircraft_template_manager",
                        "can export aircraft template manager",
                    ],
                ],
            },
        ),
    ]

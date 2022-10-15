# Generated by Django 4.1.2 on 2022-10-07 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "aircraft_template_manager",
            "0005_alter_aircrafttemplatemanager_year_manufactured",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aircrafttemplatemanager",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    [
                        "deactivate_aircrafttemplatemanager",
                        "can deactivate aircraft template manager",
                    ],
                    [
                        "print_aircrafttemplatemanager",
                        "can print aircraft template manager",
                    ],
                    [
                        "import_aircrafttemplatemanager",
                        "can import aircraft template manager",
                    ],
                    [
                        "export_aircrafttemplatemanager",
                        "can export aircraft template manager",
                    ],
                ],
            },
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-07 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_settings", "0006_alter_damagetoaircraft_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="damagetoaircraft",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    ["deactivate_damagetoaircraft", "can deactivate data settings"],
                    ["print_amagetoaircraft", "can print data settings"],
                    ["import_amagetoaircraft", "can import data settings"],
                    ["export_amagetoaircraft", "can export data settings"],
                ],
            },
        ),
        migrations.AlterModelOptions(
            name="highestinjurylevel",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    [
                        "deactivate_highestinjurylevel",
                        "can deactivate highest injury level",
                    ],
                    ["print_highestinjurylevel", "can print highest injury level"],
                    ["import_highestinjurylevel", "can import highest injury level"],
                    ["export_highestinjurylevel", "can export highest injury level"],
                ],
            },
        ),
        migrations.AlterModelOptions(
            name="investigationstatus",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    [
                        "deactivate_investigationstatus",
                        "can deactivate investigation status",
                    ],
                    ["print_investigationstatus", "can print investigation status"],
                    ["import_investigationstatus", "can import investigation status"],
                    ["export_investigationstatus", "can export investigation status"],
                ],
            },
        ),
        migrations.AlterModelOptions(
            name="occurrencecategory",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    [
                        "deactivate_occurrencecategory",
                        "can deactivate occurrence category",
                    ],
                    ["print_occurrencecategory", "can print occurrence category"],
                    ["import_occurrencecategory", "can import occurrence category"],
                    ["export_occurrencecategory", "can export occurrence category"],
                ],
            },
        ),
        migrations.AlterModelOptions(
            name="occurrencetype",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    ["deactivate_occurrencetype", "can deactivate occurrence type"],
                    ["print_occurrencetype", "can print occurrence type"],
                    ["import_occurrencetype", "can import occurrence type"],
                    ["export_occurrencetype", "can export occurrence type"],
                ],
            },
        ),
        migrations.AlterModelOptions(
            name="reportstatus",
            options={
                "ordering": ["-created_at"],
                "permissions": [
                    ["deactivate_reportstatus", "can deactivate report status"],
                    ["print_reportstatus", "can print report status"],
                    ["import_reportstatus", "can import report status"],
                    ["export_reportstatus", "can export report status"],
                ],
            },
        ),
    ]

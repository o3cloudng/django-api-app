# Generated by Django 4.1.1 on 2022-10-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "aircraft_template_manager",
            "0004_alter_aircrafttemplatemanager_year_manufactured",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircrafttemplatemanager",
            name="year_manufactured",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aircraft_template_manager", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aircrafttemplatemanager",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="aircrafttemplatemanager",
            name="model_3d_image",
            field=models.ImageField(upload_to="model_3d_image//%Y/%m/%d"),
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-16 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="administrator",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="committee",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="occurrenceareamanager",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="occurrenceowner",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="stakeholder",
            options={"ordering": ["-id"]},
        ),
    ]

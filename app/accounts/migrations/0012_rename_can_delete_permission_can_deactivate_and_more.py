# Generated by Django 4.1.1 on 2022-09-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_remove_user_role_role_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="permission",
            old_name="can_delete",
            new_name="can_deactivate",
        ),
        migrations.RenameField(
            model_name="permission",
            old_name="can_update",
            new_name="can_edit",
        ),
        migrations.AddField(
            model_name="permission",
            name="can_activate",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="permission",
            name="can_print",
            field=models.BooleanField(default=False, null=True),
        ),
    ]

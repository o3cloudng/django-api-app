# Generated by Django 4.1.1 on 2022-09-21 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_permissions_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="permissions",
            name="can_export",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="permissions",
            name="can_import",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="permissions",
            name="can_add",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="permissions",
            name="can_delete",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="permissions",
            name="can_update",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="permissions",
            name="can_view",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="permissions",
            name="model",
            field=models.CharField(
                choices=[("GENERAL", "General"), ("User", "User"), ("Role", "Role")],
                default="GENERAL",
                max_length=500,
            ),
        ),
        migrations.RemoveField(
            model_name="user",
            name="role",
        ),
        migrations.CreateModel(
            name="UserRole",
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
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="accounts.role"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ManyToManyField(
                through="accounts.UserRole", to="accounts.role"
            ),
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-28 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_alter_user_deleted_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="role",
            name="user",
        ),
        migrations.AlterUniqueTogether(
            name="userrole",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="userrole",
            name="role",
        ),
        migrations.RemoveField(
            model_name="userrole",
            name="user",
        ),
        migrations.DeleteModel(
            name="Permission",
        ),
        migrations.DeleteModel(
            name="Role",
        ),
        migrations.DeleteModel(
            name="UserRole",
        ),
    ]
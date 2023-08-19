# Generated by Django 4.2.4 on 2023-08-19 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_userprofile_invite_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="activated_invite",
            field=models.CharField(blank=True, default="1", max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="invite_code",
            field=models.CharField(blank=True, default="exit", max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="verification_code",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.CreateModel(
            name="UserInvite",
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
                ("invite_code", models.CharField(max_length=6)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invites",
                        to="main.userprofile",
                    ),
                ),
            ],
        ),
    ]
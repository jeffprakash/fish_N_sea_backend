# Generated by Django 4.1.3 on 2022-12-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_rename_user2_fish1_fishermen_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="fishcount",
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
                ("name", models.TextField()),
                ("rating", models.IntegerField()),
            ],
        ),
    ]
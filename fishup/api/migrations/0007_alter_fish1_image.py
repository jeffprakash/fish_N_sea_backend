# Generated by Django 4.1.3 on 2022-12-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_fish1_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fish1",
            name="image",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.8 on 2023-12-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("initial_access", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="initaccess",
            name="option_A",
            field=models.CharField(default="yes", max_length=200),
        ),
        migrations.AlterField(
            model_name="initaccess",
            name="option_B",
            field=models.CharField(default="no", max_length=200),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0037_merge_20240619_2223"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apiauthtoken",
            options={"verbose_name": "API Key", "verbose_name_plural": "API Keys"},
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-08 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wallet",
            old_name="wallet_name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="wallet",
            old_name="user_id",
            new_name="user",
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0002_alter_bankaccount_account_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankaccount",
            name="account_number",
            field=models.IntegerField(unique=True),
        ),
    ]
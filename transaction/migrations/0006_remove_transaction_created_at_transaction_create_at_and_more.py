# Generated by Django 5.1.3 on 2025-01-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0005_transaction_created_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="created_at",
        ),
        migrations.AddField(
            model_name="transaction",
            name="create_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

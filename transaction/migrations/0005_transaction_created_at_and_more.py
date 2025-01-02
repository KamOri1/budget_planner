# Generated by Django 5.1.3 on 2025-01-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0004_alter_transaction_transaction_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=0.0004940711462450593
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_date",
            field=models.DateTimeField(),
        ),
    ]

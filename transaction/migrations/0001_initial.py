# Generated by Django 5.1.3 on 2025-01-03 21:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0004_rename_user_category_user_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("sum_amount", models.FloatField()),
                ("description", models.TextField()),
                ("transaction_name", models.CharField(default="", max_length=100)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("transaction_date", models.DateTimeField()),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.category",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

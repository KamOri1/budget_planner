# Generated by Django 5.1.6 on 2025-02-18 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0002_categorytype_alter_category_category_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_type",
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name="CategoryType",
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryManagementSystem", "0014_delete_fine"),
    ]

    operations = [
        migrations.AlterField(
            model_name="overduebook",
            name="fine_amount",
            field=models.CharField(default="10 dollars", max_length=20),
        ),
    ]

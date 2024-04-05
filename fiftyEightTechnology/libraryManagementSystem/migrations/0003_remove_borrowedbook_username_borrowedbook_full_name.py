# Generated by Django 4.2.11 on 2024-04-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libraryManagementSystem", "0002_borrowedbook_fine"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="borrowedbook",
            name="username",
        ),
        migrations.AddField(
            model_name="borrowedbook",
            name="full_name",
            field=models.CharField(default="Enter your full name", max_length=50),
        ),
    ]

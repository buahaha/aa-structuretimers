# Generated by Django 2.2.13 on 2020-08-03 19:10

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("timerboard2", "0007_auto_20200803_1906"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationrule",
            name="minutes",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[("M00", "0"), ("M05", "5"), ("M15", "15"), ("M30", "30")],
                help_text="Time before event in minutes when notifications are sent",
                max_length=15,
            ),
        ),
    ]
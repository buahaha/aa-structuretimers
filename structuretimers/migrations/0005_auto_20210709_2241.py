# Generated by Django 3.1.12 on 2021-07-09 22:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveuniverse", "0005_type_materials_and_sections"),
        ("eveonline", "0014_auto_20210105_1413"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("structuretimers", "0004_auto_20210709_2205"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timer",
            name="eve_alliance",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Alliance of the user who created this timer",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="eveonline.eveallianceinfo",
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="eve_character",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Main character of the user who created this timer",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="eveonline.evecharacter",
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="eve_corporation",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text="Corporation of the user who created this timer",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="eveonline.evecorporationinfo",
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="eve_solar_system",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="eveuniverse.evesolarsystem",
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="structure_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="eveuniverse.evetype",
            ),
        ),
        migrations.AlterField(
            model_name="timer",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

# Generated by Django 2.2.13 on 2020-08-07 20:51

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0012_index_additions"),
        ("structuretimers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_alliances",
            field=models.ManyToManyField(
                blank=True,
                help_text="Timer must NOT be created by one of the given alliances",
                related_name="notification_rule_exclude_alliances",
                to="eveonline.EveAllianceInfo",
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_corporations",
            field=models.ManyToManyField(
                blank=True,
                help_text="Timer must NOT be created by one of the given corporations",
                related_name="notification_rule_exclude_corporations",
                to="eveonline.EveCorporationInfo",
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_important",
            field=models.BooleanField(
                default=False, help_text="Timer must NOT be important"
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_objectives",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("UN", "undefined"),
                    ("HO", "hostile"),
                    ("FR", "friendly"),
                    ("NE", "neutral"),
                ],
                help_text="Timer must NOT have one of the given objectives",
                max_length=11,
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_opsec",
            field=models.BooleanField(
                default=False, help_text="Timer must NOT be OPSEC"
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_timer_types",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("NO", "Unspecified"),
                    ("AR", "Armor"),
                    ("HL", "Hull"),
                    ("FI", "Final"),
                    ("AN", "Anchoring"),
                    ("UA", "Unanchoring"),
                    ("MM", "Moon Mining"),
                ],
                help_text="Timer must NOT have one of the given timer types",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="exclude_visibility",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("UN", "unrestricted"),
                    ("AL", "Alliance only"),
                    ("CO", "Corporation only"),
                ],
                help_text="Visibility must NOT be one of the selected",
                max_length=8,
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="require_important",
            field=models.BooleanField(
                default=False, help_text="Timer must be important"
            ),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="require_opsec",
            field=models.BooleanField(default=False, help_text="Timer must be OPSEC"),
        ),
        migrations.AddField(
            model_name="notificationrule",
            name="require_visibility",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("UN", "unrestricted"),
                    ("AL", "Alliance only"),
                    ("CO", "Corporation only"),
                ],
                help_text="Visibility must be one of the selectedor leave blank to match any.",
                max_length=8,
            ),
        ),
        migrations.AlterField(
            model_name="notificationrule",
            name="minutes",
            field=models.PositiveIntegerField(
                choices=[
                    (0, "0"),
                    (5, "5"),
                    (10, "10"),
                    (15, "15"),
                    (30, "30"),
                    (45, "45"),
                    (60, "60"),
                    (90, "90"),
                    (120, "120"),
                ],
                db_index=True,
                help_text="Time before event in minutes when notifications are sent",
            ),
        ),
        migrations.AlterField(
            model_name="notificationrule",
            name="require_alliances",
            field=models.ManyToManyField(
                blank=True,
                help_text="Timer must be created by one of the given alliances or leave blank to match any.",
                related_name="notification_rule_require_alliances",
                to="eveonline.EveAllianceInfo",
            ),
        ),
        migrations.AlterField(
            model_name="notificationrule",
            name="require_corporations",
            field=models.ManyToManyField(
                blank=True,
                help_text="Timer must be created by one of the given corporations or leave blank to match any.",
                related_name="notification_rule_require_corporations",
                to="eveonline.EveCorporationInfo",
            ),
        ),
    ]

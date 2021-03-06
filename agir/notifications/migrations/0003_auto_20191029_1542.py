# Generated by Django 2.2.6 on 2019-10-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0002_rename_models")]

    operations = [
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                condition=models.Q(link__startswith="http://agir.local:8000"),
                fields=["link"],
                name="internal_links",
            ),
        )
    ]

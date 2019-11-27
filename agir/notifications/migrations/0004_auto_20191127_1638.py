# Generated by Django 2.2.7 on 2019-11-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20191029_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='icon',
            field=models.CharField(blank=True, help_text='Indiquez le nom d\'une icône dans <a href="https://fontawesome.com/v4.7.0/icons/">cette liste</a>', max_length=200, verbose_name='icône'),
        ),
    ]

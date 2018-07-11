# Generated by Django 2.0.6 on 2018-06-13 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0050_add_foreign_keys_to_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='event_images', to='people.Person'),
        ),
        migrations.AlterField(
            model_name='identifiedguest',
            name='status',
            field=models.CharField(choices=[('AP', 'En attente du paiement'), ('CO', 'Inscription confirmée'), ('CA', 'Inscription annulée')], default='CO', max_length=2, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='status',
            field=models.CharField(choices=[('AP', 'En attente du paiement'), ('CO', 'Inscription confirmée'), ('CA', 'Inscription annulée')], default='CO', max_length=2, verbose_name='Statut'),
        ),
    ]
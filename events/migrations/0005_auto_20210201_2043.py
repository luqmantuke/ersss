# Generated by Django 3.1.5 on 2021-02-01 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='event_name',
            new_name='name',
        ),
    ]
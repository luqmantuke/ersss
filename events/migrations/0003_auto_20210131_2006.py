# Generated by Django 3.1.5 on 2021-01-31 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210131_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['-date']},
        ),
    ]

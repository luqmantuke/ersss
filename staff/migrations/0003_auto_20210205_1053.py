# Generated by Django 3.1.5 on 2021-02-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='category',
            field=models.CharField(choices=[('Teaching Staff', 'Teaching Staff'), ('Non-Teaching Staff', 'Non-Teaching Staff')], max_length=50),
        ),
    ]

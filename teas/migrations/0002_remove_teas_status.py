# Generated by Django 3.0.8 on 2020-12-31 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teas',
            name='status',
        ),
    ]

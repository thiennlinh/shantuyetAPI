# Generated by Django 3.0.8 on 2021-01-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acreage', models.FloatField(blank=True, max_length=20, null=True)),
                ('number_tea', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]

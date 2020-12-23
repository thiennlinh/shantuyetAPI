# Generated by Django 3.0.8 on 2020-12-23 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('fullname', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=30)),
                ('gender', models.BooleanField(default=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('dob', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('approved', 'Approved'), ('reject', 'Reject')], default='processing', max_length=20)),
                ('user_type', models.CharField(choices=[('owner', 'Owner'), ('secondary_owner', 'SecondaryOwner')], default='secondary_owner', max_length=20)),
                ('id_card', models.CharField(blank=True, max_length=12, null=True)),
                ('permanent_residence', models.CharField(blank=True, max_length=2000, null=True)),
                ('issued_by', models.CharField(blank=True, max_length=1000, null=True)),
                ('issued_date', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
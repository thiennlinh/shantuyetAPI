# Generated by Django 3.0.8 on 2020-12-31 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
        ('teas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('approved', 'Approved'), ('reject', 'Reject')], default='processing', max_length=20)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='userprofile.Owner')),
                ('secondary_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_owner', to='userprofile.SecondaryOwner')),
                ('tea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teas.Teas')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

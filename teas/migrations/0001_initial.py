# Generated by Django 3.0.8 on 2021-01-18 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treearea', '0001_initial'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('diameter', models.IntegerField(blank=True, null=True)),
                ('height', models.FloatField(max_length=2000, null=True)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=15)),
                ('lon', models.DecimalField(decimal_places=9, max_digits=15)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('reject', 'Reject'), ('processing', 'Processing')], default='processing', max_length=20)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='teas/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='teas/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='teas/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='teas/%Y/%m/%d')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.Owner')),
                ('tree_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='treearea.TreeArea')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

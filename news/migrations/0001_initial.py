# Generated by Django 3.0.8 on 2021-01-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=2000, null=True)),
                ('short_content', models.CharField(max_length=2000, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='news/%Y/%m/%d/')),
                ('is_hot', models.BooleanField(default=False)),
                ('is_enable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

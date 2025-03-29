# Generated by Django 5.1.7 on 2025-03-29 14:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDays',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RequestResource',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('available_days', models.ManyToManyField(blank=True, to='Organization.availabledays')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_resource', to='Organization.resource')),
            ],
        ),
    ]

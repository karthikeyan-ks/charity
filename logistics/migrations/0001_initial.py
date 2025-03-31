# Generated by Django 5.1.7 on 2025-03-30 17:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0005_requestresource_created_at'),
        ('donations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryRequest',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('accept', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('delivered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_delivered_by', to=settings.AUTH_USER_MODEL)),
                ('delivered_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_delivered_to', to=settings.AUTH_USER_MODEL)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_donation', to='donations.donations')),
                ('logistic_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_logistic_partner', to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_organization', to='Organization.requestresource')),
            ],
        ),
    ]

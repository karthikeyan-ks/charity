# Generated by Django 5.1.7 on 2025-03-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_donor_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='phone',
        ),
        migrations.AddField(
            model_name='donor',
            name='address',
            field=models.TextField(default='address 1'),
        ),
        migrations.AddField(
            model_name='donor',
            name='pincode',
            field=models.CharField(default='123456', max_length=6),
        ),
    ]

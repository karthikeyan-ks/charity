# Generated by Django 5.1.7 on 2025-03-30 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0003_requestresource_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestresource',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

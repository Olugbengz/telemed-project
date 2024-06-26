# Generated by Django 4.2.7 on 2024-04-09 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient_record', '0002_patientrecord_record_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='new_appointment',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='record_owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

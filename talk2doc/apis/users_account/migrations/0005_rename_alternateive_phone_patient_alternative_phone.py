# Generated by Django 4.2.7 on 2023-12-05 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_account', '0004_rename_hospital_doctor_hospital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='alternateive_phone',
            new_name='alternative_phone',
        ),
    ]

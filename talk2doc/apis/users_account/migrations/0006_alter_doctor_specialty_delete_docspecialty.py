# Generated by Django 4.2.7 on 2023-12-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_account', '0005_rename_alternateive_phone_patient_alternative_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(choices=[('INTERNAL MEDICINE', 'Internal Medicine'), ('PEDIATRICIAN', 'Pediatrician'), ('ORTHOPEDIST', 'Orthopedist'), ('PSYCHIATRIST', 'Psychiatrist'), ('UROLOGIST', 'Urologist'), ('PATHOLOGIST', 'Pathologist'), ('NEUROLOGIST', 'Neurologist'), ('GASTROENTEROLOGIST', 'Gastroenterologist'), ('ANESTHESIOLOGIST', 'Anesthesiologist'), ('OBSTERICIAN', 'Obsterician'), ('GYNAECOLOGIST', 'Gynaecologist'), ('DERMATOLOGIST', 'Dermatologist'), ('RHEUMATOLOGIST', 'Rheumatologist'), ('OPHTHALMOLOGIST', 'Ophthalmologist'), ('CARDIOLOGIST', 'Cardiologist'), ('FAMILY MEDICINE', 'Family Medicine'), ('RADIOLOGIST', 'Radiologist'), ('NEUROLOGIST', 'Neurologist'), ('ONCOLOGIST', 'Oncologist'), ('NEPHEROLOGIST', 'Nepherologist')], default='Family Medicine', max_length=30),
        ),
        migrations.DeleteModel(
            name='DocSpecialty',
        ),
    ]

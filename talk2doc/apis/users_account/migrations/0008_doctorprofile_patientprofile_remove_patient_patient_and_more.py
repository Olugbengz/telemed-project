# Generated by Django 4.2.7 on 2024-04-09 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_account', '0007_remove_patient_patient_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(choices=[('INTERNAL MEDICINE', 'Internal Medicine'), ('PEDIATRICIAN', 'Pediatrician'), ('ORTHOPEDIST', 'Orthopedist'), ('PSYCHIATRIST', 'Psychiatrist'), ('UROLOGIST', 'Urologist'), ('PATHOLOGIST', 'Pathologist'), ('NEUROLOGIST', 'Neurologist'), ('GASTROENTEROLOGIST', 'Gastroenterologist'), ('ANESTHESIOLOGIST', 'Anesthesiologist'), ('OBSTERICIAN', 'Obsterician'), ('GYNAECOLOGIST', 'Gynaecologist'), ('DERMATOLOGIST', 'Dermatologist'), ('RHEUMATOLOGIST', 'Rheumatologist'), ('OPHTHALMOLOGIST', 'Ophthalmologist'), ('CARDIOLOGIST', 'Cardiologist'), ('FAMILY MEDICINE', 'Family Medicine'), ('RADIOLOGIST', 'Radiologist'), ('NEUROLOGIST', 'Neurologist'), ('ONCOLOGIST', 'Oncologist'), ('NEPHEROLOGIST', 'Nepherologist')], default='Family Medicine', max_length=30)),
                ('language', models.CharField(choices=[('English', 'English'), ('Hausa', 'Hausa'), ('Igbo', 'Igbo'), ('Yoruba', 'Yoruba')], default='ENGLISH', max_length=15)),
                ('location', models.CharField(max_length=20)),
                ('hospital', models.CharField(max_length=30)),
                ('years_of_experience', models.CharField(max_length=2)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Others')], default='Others', max_length=7)),
                ('alternative_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=30, null=True)),
                ('emergency_contact_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('emergency_contact_relationship', models.CharField(blank=True, max_length=20, null=True)),
                ('medical_plan', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='patient',
        ),
        migrations.AddField(
            model_name='telemeduser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='telemeduser',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='telemeduser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='telemeduser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users_account.telemeduser',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users_account.telemeduser',),
        ),
    ]
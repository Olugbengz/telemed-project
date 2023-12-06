# Generated by Django 4.2.7 on 2023-12-03 07:07

import apis.users_account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_record', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeleMedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocSpecialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(choices=[('INTERNAL MEDICINE', 'Internal Medicine'), ('PEDIATRICIAN', 'Pediatrician'), ('ORTHOPEDIST', 'Orthopedist'), ('PSYCHIATRIST', 'Psychiatrist'), ('UROLOGIST', 'Urologist'), ('PATHOLOGIST', 'Pathologist'), ('NEUROLOGIST', 'Neurologist'), ('GASTROENTEROLOGIST', 'Gastroenterologist'), ('ANESTHESIOLOGIST', 'Anesthesiologist'), ('OBSTERICIAN', 'Obsterician'), ('GYNAECOLOGIST', 'Gynaecologist'), ('DERMATOLOGIST', 'Dermatologist'), ('RHEUMATOLOGIST', 'Rheumatologist'), ('OPHTHALMOLOGIST', 'Ophthalmologist'), ('CARDIOLOGIST', 'Cardiologist'), ('FAMILY MEDICINE', 'Family Medicine'), ('RADIOLOGIST', 'Radiologist'), ('NEUROLOGIST', 'Neurologist'), ('ONCOLOGIST', 'Oncologist'), ('NEPHEROLOGIST', 'Nepherologist')], default='FAMILY MEDICINE', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Others', 'Others')], default='Others', max_length=7)),
                ('alternateive_phone', models.CharField(max_length=15)),
                ('emergency_contact_name', models.CharField(max_length=30)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('emergency_contact_relationship', models.CharField(max_length=20)),
                ('medical_plan', models.CharField(max_length=20)),
                ('nin', models.IntegerField()),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=apis.users_account.models.TeleMedUser)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_record.patientrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('Hausa', 'Hausa'), ('Igbo', 'Igbo'), ('Yoruba', 'Yoruba')], default='ENGLISH', max_length=15)),
                ('location', models.CharField(max_length=20)),
                ('Hospital', models.CharField(max_length=30)),
                ('years_of_experience', models.CharField(max_length=2)),
                ('about', models.TextField()),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=apis.users_account.models.TeleMedUser)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_specialty', to='users_account.docspecialty')),
            ],
        ),
        migrations.CreateModel(
            name='DocAvailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
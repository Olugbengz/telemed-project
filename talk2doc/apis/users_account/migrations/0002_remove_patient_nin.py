# Generated by Django 4.2.7 on 2023-12-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='nin',
        ),
    ]
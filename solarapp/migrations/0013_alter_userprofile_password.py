# Generated by Django 4.2.9 on 2024-02-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarapp', '0012_alter_installer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$4hBcq97Jdv1jHf3nz688i0$zQ5TOEetTzpiLTopXIChLXI11Ag8YhOj+6+bFrAbuOg=', max_length=100),
        ),
    ]

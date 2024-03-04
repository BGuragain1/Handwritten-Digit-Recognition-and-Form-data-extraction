# Generated by Django 5.0.1 on 2024-02-26 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScanForm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NomineeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('citizenship_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('house_no', models.CharField(max_length=255)),
                ('vdc', models.CharField(max_length=255)),
                ('ward_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('citizenship_no', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('issued_district', models.CharField(max_length=255)),
                ('issued_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('house_no', models.CharField(max_length=255)),
                ('vdc', models.CharField(max_length=255)),
                ('ward_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='FormDetails',
        ),
    ]

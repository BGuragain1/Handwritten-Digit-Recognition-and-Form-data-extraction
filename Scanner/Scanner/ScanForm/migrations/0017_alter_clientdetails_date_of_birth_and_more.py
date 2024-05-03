# Generated by Django 5.0.1 on 2024-04-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScanForm', '0016_alter_clientdetails_higher_secondary_cgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdetails',
            name='date_of_birth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='guardian_phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='higher_secondary_cgpa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='higher_secondary_year_completion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='permanent_ward_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='permanent_zip_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='secondary_cgpa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='secondary_year_completion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='temporary_ward_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdetails',
            name='temporary_zip_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

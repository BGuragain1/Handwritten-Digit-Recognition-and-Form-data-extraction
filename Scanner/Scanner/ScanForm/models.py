from django.db import models

from django.db import models

class PersonalInfo(models.Model):
    user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    issued_district = models.CharField(max_length=255)
    issued_date = models.DateField()

class NomineeInfo(models.Model):
    user_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=255)

class TemporaryAddress(models.Model):
    user_id = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    house_no = models.CharField(max_length=255)
    vdc = models.CharField(max_length=255)
    ward_no = models.CharField(max_length=255)

class PermanentAddress(models.Model):
    user_id = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    house_no = models.CharField(max_length=255)
    vdc = models.CharField(max_length=255)
    ward_no = models.CharField(max_length=255)


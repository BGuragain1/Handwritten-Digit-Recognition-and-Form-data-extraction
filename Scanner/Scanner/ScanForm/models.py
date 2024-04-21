from django.db import models
from django.utils import timezone


class ClientDetails(models.Model):
    user_id = models.CharField(max_length=255)
    form_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    citizenship_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    issued_district = models.CharField(max_length=255)
    issued_date = models.CharField(max_length=255)
    first_name_nominee = models.CharField(max_length=255)
    middle_name_nominee = models.CharField(max_length=255)
    last_name_nominee = models.CharField(max_length=255)
    citizenship_no_nominee = models.CharField(max_length=255)
    temp_district = models.CharField(max_length=255)
    temp_house_no = models.CharField(max_length=255)
    temp_vdc = models.CharField(max_length=255)
    temp_ward_no = models.CharField(max_length=255)
    perm_user_id = models.CharField(max_length=255)
    perm_district = models.CharField(max_length=255)
    perm_house_no = models.CharField(max_length=255)
    perm_vdc = models.CharField(max_length=255)
    perm_ward_no = models.CharField(max_length=255)
    uploaded_date = models.DateTimeField(null=True)
    status = models.CharField(default="pending",max_length=255)

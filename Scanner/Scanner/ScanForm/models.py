from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    
class StudentDetails(models.Model):
    user_id = models.CharField(max_length=100,null=True)
    form_name = models.CharField(max_length=100,null=True)
    uploaded_time = models.DateTimeField(default=timezone.now)

    #general information
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    date_of_birth = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    citizenship_number = models.CharField(max_length=20, null=True)

    # Course for Enrollment
    course = models.CharField(max_length=100, null=True)

    # Guardian Information
    guardian_first_name = models.CharField(max_length=100, null=True)
    guardian_middle_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_last_name = models.CharField(max_length=100, null=True)
    guardian_phone_number = models.CharField(max_length=100, null=True)
    relation_to_student = models.CharField(max_length=100, null=True)

    # Education Section - Secondary Level
    secondary_school_name = models.CharField(max_length=100, null=True)
    secondary_year_completion = models.CharField(max_length=100, null=True)
    secondary_cgpa = models.CharField(max_length=100, null=True)
    secondary_district = models.CharField(max_length=100, null=True)
    secondary_municipality = models.CharField(max_length=100, null=True)
    secondary_wardno = models.CharField(max_length=100, null=True)

    # Education Section - Higher Secondary Level
    higher_secondary_school_name = models.CharField(max_length=100, null=True)
    higher_secondary_year_completion = models.CharField(max_length=100, null=True)
    higher_secondary_cgpa = models.CharField(max_length=100, null=True)
    higher_secondary_district = models.CharField(max_length=100, null=True)
    higher_secondary_municipality = models.CharField(max_length=100,null=True)
    higher_secondary_faculty = models.CharField(max_length=100,null=True)
    higher_secondary_wardno = models.CharField(max_length=100, null=True)

    # Permanent Address
    permanent_province = models.CharField(max_length=100, null=True)
    permanent_district = models.CharField(max_length=100, null=True)
    permanent_municipality = models.CharField(max_length=100, null=True)
    permanent_ward_no = models.CharField(max_length=100, null=True)
    permanent_tole = models.CharField(max_length=100, null=True)

    # Temporary Address
    temporary_province = models.CharField(max_length=100, null=True)
    temporary_district = models.CharField(max_length=100, null=True)
    temporary_municipality = models.CharField(max_length=100, null=True)
    temporary_ward_no = models.CharField(max_length=100, null=True)
    temporary_tole = models.CharField(max_length=100, null=True)
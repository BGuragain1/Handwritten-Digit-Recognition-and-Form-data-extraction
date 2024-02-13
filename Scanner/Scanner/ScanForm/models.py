from django.db import models

# Create your models here.
class FormDetails(models.Model):
    name = models.CharField(max_length =122 )
    email = models.CharField(max_length = 122 )
    phone = models.CharField(max_length = 12 )
    citizenNum = models.CharField(max_length = 122 )
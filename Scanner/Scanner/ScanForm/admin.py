from django.contrib import admin
from ScanForm.models import PersonalInfo,NomineeInfo,TemporaryAddress,PermanentAddress

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(NomineeInfo)
admin.site.register(TemporaryAddress)
admin.site.register(PermanentAddress)
from django.contrib import admin
from .models import *
# Register your models here.

class PostPatient(admin.ModelAdmin):
    list_display=['patient_id','name','age','phone','visitdate']
admin.site.register(Patient,PostPatient)
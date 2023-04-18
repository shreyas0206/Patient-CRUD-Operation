from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=2)
    phone=models.CharField(max_length=10)
    Details = models.TextField()
    visitdate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# admin
# admin
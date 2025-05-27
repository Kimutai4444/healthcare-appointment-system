from django.db import models

# Create your models here.
class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"

    
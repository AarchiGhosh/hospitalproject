from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    phone_no = models.CharField(max_length = 10)
    is_doctor = models.BooleanField('doctor status', default=False)
    USERNAME_FIELD = 'username'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialisation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.user.username}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=4)
    height_in_cm = models.IntegerField(default=160)
    weight_in_kg = models.IntegerField(default=50)
    diagnosis = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class Availability(models.Model):
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

from django.db import models

# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    p_no=models.CharField(max_length=10, unique=True)
    password=models.CharField(max_length=10)
    c_password=models.CharField(max_length=10)

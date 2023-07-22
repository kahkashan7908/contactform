from django.db import models
class empData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=50)

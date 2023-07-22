from django.db import models
class studentData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    emil=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    iname=models.CharField(max_length=50)
    fee=models.IntegerField()
    marks=models.IntegerField()
    location=models.CharField(max_length=50)
    
    

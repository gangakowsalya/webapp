from django.db import models

class test1(models.Model):
    username = models.CharField(default = "" , max_length = 20)
    email = models.EmailField(default = "",max_length =  100)
    password = models.CharField(default = "",max_length=20) 
    

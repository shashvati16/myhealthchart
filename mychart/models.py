from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()

class Covidtest(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    covidtest = models.IntegerField()
    testtype = models.CharField(max_length=50)
    testdate = models.DateTimeField()

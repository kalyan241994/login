from django.db import models


class signUp(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=200)


    def __unicode__(self):
    	return self.username

    def __str__(self):
    	return self.username
# Create your models here.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class User(models.Model):
        time = models.DateField(auto_now_add=True)
	nama = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=15)
        pekerjaan=models.CharField(max_length=100)
        institusi = models.CharField(max_length=100)
        def __str__(self):
                return self.nama


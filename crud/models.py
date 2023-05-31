import django
from django.db import models
from datetime import datetime
from django.conf import settings
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.
class Department (models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255)
    description = models.TextField()
   
    def __str__(self):
        return self.name



class Course(models.Model):
    course_id = models.IntegerField()
    course_name = models.CharField(max_length=255)
    course_discription = models.TextField()
    
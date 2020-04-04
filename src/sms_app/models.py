from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Element(models.Model):
    element_name = models.CharField(max_length=100, unique=True)
    element_number = models.IntegerField(unique=True)
    element_description = models.TextField()

    def __str__(self):
        return self.element_name 

class Process(models.Model):
    process_name = models.CharField(max_length=250, unique=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    process_number = models.IntegerField(unique=True)
    element = models.ForeignKey(Element, related_name='process' ,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='process', on_delete=models.CASCADE)

class Kpi(models.Model):
    kpi_name = models.CharField(max_length=250)
    process = models.ForeignKey(Process, related_name='kpi' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='kpi', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)

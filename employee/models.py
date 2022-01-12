from django.db import models

class Employee(models.Model):
    name = models.TextField()
    email = models.TextField()
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)


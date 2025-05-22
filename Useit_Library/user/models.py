from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('regular_user', 'Regular User'),
        ('admin', 'Admin'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"

from django.db import models

# Create your models here.
class Institution(models.Model):
    name = models.CharField(max_length=200)
    institution_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} ({self.institution.name})"
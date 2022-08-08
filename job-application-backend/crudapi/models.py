from django.db import models

# Create your models here.
class Userjob(models.Model):
    email = models.CharField(max_length=50)
    jobId = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
class Jobapplication(models.Model):
    jobId = models.CharField(max_length=50)
    status_choices =   (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    status = models.CharField(max_length = 1,choices=status_choices)
    website = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=50)
    jobDescription = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

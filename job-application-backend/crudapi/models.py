from django.db import models

# Create your models here.
Class UserJob(models.Model):
    email = models.CharField(max_length=50)
    jobId = models.CharField(max_length=50)

Class JobApplication(models.Model):
    jobId = models.CharField(max_length=50)
    status =   (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    company = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=50)
    jobDescription = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
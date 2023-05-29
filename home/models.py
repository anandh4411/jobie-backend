from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # skills = models.JSONField()
    def __str__(self) -> str:
        return self.name
    
class UserFiles(models.Model):
    user_id = models.IntegerField()
    profile_image = models.ImageField(upload_to="user-profile", blank=True)
    cover_image = models.ImageField(upload_to="user-cover", blank=True)
    resume = models.FileField(upload_to="user-resume", blank=True)

class HR(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    
class Company(models.Model):
    company_id = models.IntegerField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="company-profile", blank=True)
    cover_image = models.ImageField(upload_to="company-cover", blank=True)
    def __str__(self) -> str:
        return self.name
    
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    company_id = models.IntegerField()
    mode = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    recruitment_type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title
    

class Application(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
    user_id = models.IntegerField()
    job_id = models.IntegerField()
    resume = models.FileField(upload_to="application-resume", blank=True)
    def __str__(self) -> str:
        return self.name
    
class Notification(models.Model):
    user = models.IntegerField()
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    notification = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    mode = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.title

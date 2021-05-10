from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)
    picture_url = models.CharField(max_length=1000)
    age = models.CharField(max_length=10)
    registered_time = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    patientID = models.CharField(max_length=20)
    fcm_token = models.CharField(max_length=1000)

class Report(models.Model):
    member_id = models.CharField(max_length=11)
    subject = models.CharField(max_length=80)
    patientID = models.CharField(max_length=50)
    body = models.CharField(max_length=8000)
    picture_url = models.CharField(max_length=1000)
    audio_url = models.CharField(max_length=1000)
    date_time = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

class Account(models.Model):
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=30)

class ReportPicture(models.Model):
    report_id = models.CharField(max_length=11)
    picture_url = models.CharField(max_length=1000)



class Field(models.Model):
    member_id = models.CharField(max_length=11)
    report_id = models.CharField(max_length=11)
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=5000)
    status = models.CharField(max_length=50)

class Template(models.Model):
    member_id = models.CharField(max_length=11)
    name = models.CharField(max_length=100)
    items_count = models.CharField(max_length=11)

class Keyword(models.Model):
    template_id = models.CharField(max_length=11)
    keyword = models.CharField(max_length=200)






















from django.db import models
from conferences.models import Conference
# Create your models here.
class Speaker(models.Model):
    name= models.CharField(max_length=100)
    bio= models.CharField(max_length=150)
    contact=models.CharField(max_length=13)
    profile_pic=models.ImageField(upload_to='profile/')


class Session(models.Model):
    topic= models.CharField(max_length=255)
    duration = models.DurationField()
    Conf_id = models.ForeignKey(Conference, on_delete=models.CASCADE)
    Speaker_id =  models.ManyToManyField(Speaker)


class Attendee(models.Model):
    Names = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100)
    Phone = models.CharField(max_length=13)
    Conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    Password = models.CharField(max_length=10, default=1234)
    Payment = models.IntegerField(default=None)
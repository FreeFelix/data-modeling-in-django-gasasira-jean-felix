import datetime
from datetime import timedelta

# https://djangoproject.com

# from conferences import models
from django.db import models
from django import forms
from .models import ScheduleManager
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name
#

#  1 cat -------> Many conf
#  1 conf ------> 1 cat:


# class Conference(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.title} - {self.category}"
class Conference(models.Model):
    Name = models.CharField(max_length=200)
    Category = models.CharField(max_length=100)
    Date = models.DateTimeField()
    Venue = models.CharField(max_length=100)
    Theme = models.CharField(max_length=100)
    # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)


class ScheduleManager(models.Model):
    Session = models.ForeignKey(Conference, on_delete=models.CASCADE)
    Start_time = models.TimeField()
    End_time = models.TimeField()
    Speaker = models.CharField(max_length=100)
    Duration = models.TimeField()



class ScheduleForm(forms.ModelForm):
    class Meta:
        model = ScheduleManager
        fields = '__all__'
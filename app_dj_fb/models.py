# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class FBUserModel(models.Model):
    """
    Contain FB user info
    """    
    ext_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    locale = models.CharField(max_length=50)
    timezone = models.IntegerField()
    link = models.URLField()

    age_min = models.IntegerField()
    img_profile = models.URLField()
    img_cover = models.URLField()


class FBUserVisitHistory(models.Model):

    fb_user = models.ForeignKey(FBUserModel)
    visit_time = models.DateTimeField(auto_now=True)

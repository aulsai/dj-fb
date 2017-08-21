# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class FBUserModel(models.Model):
    """
    Contain FB user info
    """    
    ext_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, null=True, blank=True)
    locale = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.IntegerField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    age_min = models.IntegerField(null=True, blank=True)
    img_profile = models.URLField(null=True, blank=True)
    img_cover = models.URLField(null=True, blank=True)


class FBUserVisitHistory(models.Model):

    fb_user = models.ForeignKey(FBUserModel)
    visit_time = models.DateTimeField(auto_now=True)

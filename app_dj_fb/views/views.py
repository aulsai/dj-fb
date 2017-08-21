# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from app_dj_fb.models import FBUserModel, FBUserVisitHistory


def _bindFBUserModel(data):

    return {
        "ext_id": data['id'],
        "timezone": data['timezone'],
        "age_min": data['age_range']['min'],
        "name": data['name'],
        "gender": data['gender'],
        "locale": data['locale'],
        "link": data['link'],
        "img_cover": data['cover']['source'] if data.get('cover') is not None else None,
        "img_profile": data['picture']['data']['url']
    }


def _createOrUpdateFBUser(update_values):
    obj = None
    try:
        obj = FBUserModel.objects.get(ext_id=update_values['ext_id'])
        for key, value in update_values.iteritems():
            setattr(obj, key, value)

        # TODO - Check from Updated Date from FB API.
        obj.save()
    except FBUserModel.DoesNotExist:            
        obj = FBUserModel(**update_values)
        obj.save()
    return obj

def _createVisitingLog(fbUserObj):
    FBUserVisitHistory.objects.create(
        fb_user=fbUserObj
    )

    return FBUserVisitHistory.objects.filter(fb_user=fbUserObj).count()

def FBUserCreate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        update_values = _bindFBUserModel(data)
        fbUserObj = _createOrUpdateFBUser(update_values)

        countUserVisiting = _createVisitingLog(fbUserObj)
                
        return HttpResponse(countUserVisiting)

    return HttpResponse(request)
        

class TestView(TemplateView):
    template_name = 'app_dj_fb/home.html'

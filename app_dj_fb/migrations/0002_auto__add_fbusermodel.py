# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FBUserModel'
        db.create_table(u'app_dj_fb_fbusermodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ext_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('locale', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('timezone', self.gf('django.db.models.fields.IntegerField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('age_min', self.gf('django.db.models.fields.IntegerField')()),
            ('img_profile', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('img_cover', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'app_dj_fb', ['FBUserModel'])


    def backwards(self, orm):
        # Deleting model 'FBUserModel'
        db.delete_table(u'app_dj_fb_fbusermodel')


    models = {
        u'app_dj_fb.fbusermodel': {
            'Meta': {'object_name': 'FBUserModel'},
            'age_min': ('django.db.models.fields.IntegerField', [], {}),
            'ext_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_cover': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'img_profile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['app_dj_fb']
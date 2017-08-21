# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FBUserModel.locale'
        db.alter_column(u'app_dj_fb_fbusermodel', 'locale', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'FBUserModel.gender'
        db.alter_column(u'app_dj_fb_fbusermodel', 'gender', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'FBUserModel.img_cover'
        db.alter_column(u'app_dj_fb_fbusermodel', 'img_cover', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'FBUserModel.link'
        db.alter_column(u'app_dj_fb_fbusermodel', 'link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'FBUserModel.age_min'
        db.alter_column(u'app_dj_fb_fbusermodel', 'age_min', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FBUserModel.timezone'
        db.alter_column(u'app_dj_fb_fbusermodel', 'timezone', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'FBUserModel.img_profile'
        db.alter_column(u'app_dj_fb_fbusermodel', 'img_profile', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'FBUserModel.locale'
        db.alter_column(u'app_dj_fb_fbusermodel', 'locale', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'FBUserModel.gender'
        db.alter_column(u'app_dj_fb_fbusermodel', 'gender', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'FBUserModel.img_cover'
        db.alter_column(u'app_dj_fb_fbusermodel', 'img_cover', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'FBUserModel.link'
        db.alter_column(u'app_dj_fb_fbusermodel', 'link', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'FBUserModel.age_min'
        db.alter_column(u'app_dj_fb_fbusermodel', 'age_min', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'FBUserModel.timezone'
        db.alter_column(u'app_dj_fb_fbusermodel', 'timezone', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'FBUserModel.img_profile'
        db.alter_column(u'app_dj_fb_fbusermodel', 'img_profile', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

    models = {
        u'app_dj_fb.fbusermodel': {
            'Meta': {'object_name': 'FBUserModel'},
            'age_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ext_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'img_cover': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'img_profile': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app_dj_fb.fbuservisithistory': {
            'Meta': {'object_name': 'FBUserVisitHistory'},
            'fb_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app_dj_fb.FBUserModel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visit_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['app_dj_fb']
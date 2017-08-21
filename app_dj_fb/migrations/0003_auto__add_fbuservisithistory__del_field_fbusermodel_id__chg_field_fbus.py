# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FBUserVisitHistory'
        db.create_table(u'app_dj_fb_fbuservisithistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app_dj_fb.FBUserModel'])),
            ('visit_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'app_dj_fb', ['FBUserVisitHistory'])

        # Deleting field 'FBUserModel.id'
        db.delete_column(u'app_dj_fb_fbusermodel', u'id')


        # Changing field 'FBUserModel.ext_id'
        db.alter_column(u'app_dj_fb_fbusermodel', 'ext_id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True))
        # Adding unique constraint on 'FBUserModel', fields ['ext_id']
        db.create_unique(u'app_dj_fb_fbusermodel', ['ext_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'FBUserModel', fields ['ext_id']
        db.delete_unique(u'app_dj_fb_fbusermodel', ['ext_id'])

        # Deleting model 'FBUserVisitHistory'
        db.delete_table(u'app_dj_fb_fbuservisithistory')

        # Adding field 'FBUserModel.id'
        db.add_column(u'app_dj_fb_fbusermodel', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=99, primary_key=True),
                      keep_default=False)


        # Changing field 'FBUserModel.ext_id'
        db.alter_column(u'app_dj_fb_fbusermodel', 'ext_id', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'app_dj_fb.fbusermodel': {
            'Meta': {'object_name': 'FBUserModel'},
            'age_min': ('django.db.models.fields.IntegerField', [], {}),
            'ext_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'img_cover': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'img_profile': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timezone': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app_dj_fb.fbuservisithistory': {
            'Meta': {'object_name': 'FBUserVisitHistory'},
            'fb_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app_dj_fb.FBUserModel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'visit_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['app_dj_fb']
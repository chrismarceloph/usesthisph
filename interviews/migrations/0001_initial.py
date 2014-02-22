# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Interview'
        db.create_table(u'interviews_interview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('portrait', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('question_0', self.gf('django.db.models.fields.TextField')()),
            ('question_1', self.gf('django.db.models.fields.TextField')()),
            ('question_2', self.gf('django.db.models.fields.TextField')()),
            ('question_3', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 23, 0, 0), auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 23, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'interviews', ['Interview'])


    def backwards(self, orm):
        # Deleting model 'Interview'
        db.delete_table(u'interviews_interview')


    models = {
        u'interviews.interview': {
            'Meta': {'object_name': 'Interview'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 23, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'portrait': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question_0': ('django.db.models.fields.TextField', [], {}),
            'question_1': ('django.db.models.fields.TextField', [], {}),
            'question_2': ('django.db.models.fields.TextField', [], {}),
            'question_3': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 23, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['interviews']
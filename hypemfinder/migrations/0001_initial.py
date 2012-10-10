# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Song'
        db.create_table('hypemfinder_song', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cookie', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('post_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('download_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('hypemfinder', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Song'
        db.delete_table('hypemfinder_song')


    models = {
        'hypemfinder.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cookie': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'download_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hypemfinder']
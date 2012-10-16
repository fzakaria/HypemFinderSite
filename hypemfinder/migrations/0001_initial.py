# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SoundSong'
        db.create_table('hypemfinder_soundsong', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('song_type', self.gf('django.db.models.fields.CharField')(default='HM', max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('post_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('waveform_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('hypemfinder', ['SoundSong'])

        # Adding model 'HypemSong'
        db.create_table('hypemfinder_hypemsong', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('song_type', self.gf('django.db.models.fields.CharField')(default='HM', max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('post_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cookie', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('hypemfinder', ['HypemSong'])


    def backwards(self, orm):
        # Deleting model 'SoundSong'
        db.delete_table('hypemfinder_soundsong')

        # Deleting model 'HypemSong'
        db.delete_table('hypemfinder_hypemsong')


    models = {
        'hypemfinder.hypemsong': {
            'Meta': {'object_name': 'HypemSong'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cookie': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'download_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'song_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'song_type': ('django.db.models.fields.CharField', [], {'default': "'HM'", 'max_length': '2'}),
            'time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'hypemfinder.soundsong': {
            'Meta': {'object_name': 'SoundSong'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'download_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'song_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'song_type': ('django.db.models.fields.CharField', [], {'default': "'HM'", 'max_length': '2'}),
            'time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'waveform_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hypemfinder']
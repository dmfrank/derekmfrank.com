# $Id: models.py,v 1.1 2013-05-30 23:46:52-07 dmf - $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - mff
#
# DESCRIPTION
#   Models definition for MFF pages.
#

from django.db import models
from django.contrib import admin
#from mysite.models import SOURCE_TYPE

# MFF

class Source(models.Model):
    title = models.CharField(max_length=64)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.title


class Information(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    email = models.EmailField()
    email_name = models.CharField(max_length=32)
    contact = models.TextField()
    image = models.ImageField(upload_to="mff/img/")
    image_text = models.TextField()
    sources = models.ManyToManyField(Source)

    def __unicode__(self):
        return self.first_name + ' ' + self.middle_name[0] + '. ' + self.last_name

class Topic(models.Model):
    title = models.CharField(max_length=128)
    pretopic_list = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class TopicListBit(models.Model):
    topic = models.ForeignKey(Topic)
    body = models.TextField()

    def __unicode__(self):
        return self.body


## ADMIN

class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

class InformationAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'last_name', 'title', 'email')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

class TopicListBitAdmin(admin.ModelAdmin):
    list_display = ('body', 'topic')


## ADMIN REGISTER
admin.site.register(Source, SourceAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicListBit, TopicListBitAdmin)

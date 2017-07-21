# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 这个类就是一张数据表


class Article(models.Model):
    title = models.CharField(max_length = 32, default = 'Title')
    content = models.TextField(null = True)
    pub_time = models.DateTimeField(null = True)

    def __unicode__(self):
        return self.title

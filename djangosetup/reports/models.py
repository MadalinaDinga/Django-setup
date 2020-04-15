import datetime

from django.db import models
from django.utils import timezone


class Report(models.Model):
    report_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    report_likes = models.IntegerField(default=0)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.report_text


class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.comment_text

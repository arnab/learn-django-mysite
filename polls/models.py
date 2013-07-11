import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        formatted_date = self.pub_date.strftime("%Y-%m-%d %H:%M %Z")
        return "{0} [published: {1}]".format(self.question, formatted_date)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return "{0} [votes: {1}]".format(self.choice_text, self.votes)

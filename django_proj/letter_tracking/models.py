from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Letter(models.Model):

    class PolParties(models.TextChoices):
        D = 'D', _('Democrat')
        R = 'R', _('Republican')
        I = 'I', _('Independent')
    
    class RepSen(models.TextChoices):
        REP = 'Rep.', _('Representative')
        SEN = 'Sen.', _('Senator')

    topic = models.CharField(max_length=25)
    legislator = models.CharField(max_length=60)
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices)
    caucus = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    chamber = models.CharField(max_length=15)
    link = models.URLField("Link to letter")
    consecutive_number = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)

    @property
    def title(self):
        return str(self.date)[:10].replace('-', '.') + '.' + str(self.chamber)[0] +\
                '.' + str(self.party)[0] + '.' + str(self.topic)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})

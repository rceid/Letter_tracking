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
    
    class Chamber(models.TextChoices):
        BI = 'B', _('Bicameral')
        S = 'S', _('Senado')
        C = 'C', _('Congreso')
        
    topic = models.CharField(max_length=25)
    legislator = models.CharField(max_length=60,
                                 verbose_name=_('Legislator Name'),
                                 help_text=
                                 "Names are displayed in <em>Last Name, First Name</em> format")
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    caucus = models.CharField(max_length=100)
    description = models.TextField(verbose_name=_('Letter Description'))
    date = models.DateTimeField(help_text="Enter dates in <em>MM/DD/YYYY</em> format")
    chamber = models.CharField(max_length=9,
                                 choices=Chamber.choices,
                                 verbose_name=_('Letter\'s Chamber of Origin'))
    link = models.URLField("Letter URL")
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)
    
    @property
    def consecutive_number(self):
        daily_order = list(Letter.objects.filter(date=self.date).order_by('date'))
        return daily_order.index(self) + 1

    @property
    def title(self):
        return str(self.date)[:10].replace('-', '.') + '.' + str(self.chamber)[0] +\
                '.' + str(self.party)[0] + '.' + str(self.topic)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})



from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from warnings import filterwarnings
filterwarnings('ignore', message=r'.*received a naive datetime')

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
    
    class Statements(models.TextChoices):
        Carta = 'Carta'
        Consulta = 'Consulta'
        Declaracion = 'Declaración'
    
    class Sentiment(models.TextChoices):
        Pos = 1, _('Positive')
        Neut = 2, _('Neutral')
        Neg = 3, _('Negative')

    class Dummy(models.TextChoices):
        y = 1, _('Yes')
        n = 0, _('No')

    topic = models.CharField(max_length=25)
    legislator = models.CharField(max_length=60,
                                 verbose_name=_('Legislator Name'),
                                 help_text=
                                 "Names are displayed in <em>Last Name, First Name</em> format")
    author = models.CharField(max_length=60,
                                 verbose_name=_('Author Name'),
                                 help_text=
                                 "Names are displayed in <em>Last Name, First Name</em> format")
    cosigners = models.CharField(max_length=500)
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
    #extra attributes only used for an excel export
    specific_topic = models.CharField(max_length=100)
    kind_of_statement = models.CharField(max_length=11,
                                            choices=Statements.choices)
    positive_MX = models.CharField(max_length=8,
                                    choices=Sentiment.choices)
    MX_mentioned = models.CharField(max_length=3,
                                    choices=Dummy.choices)
    recipient = models.CharField(max_length=50)
    kind_statement_party = models.CharField(max_length=11,
                                            choices=Statements.choices)
    comments =  models.TextField()
    action = models.CharField(max_length=100)
    notice_num = models.CharField(max_length=30)


    @property
    def consecutive_number(self):
        daily_order = list(Letter.objects.filter(date=self.date).order_by('date'))
        return daily_order.index(self) + 1

    @property
    def title(self):
        return str(self.date)[:10].replace('-', '.') + '.' + str(self.chamber)[0] +\
                '.' + str(self.party) + '.' + str(self.topic) + '.' + str(self.consecutive_number)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})



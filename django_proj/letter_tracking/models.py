from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from warnings import filterwarnings
filterwarnings('ignore', message=r'.*received a naive datetime')

class Legislator(models.Model):

    class RepSen(models.TextChoices):
        REP = 'Rep.', _('Representative')
        SEN = 'Sen.', _('Senator')

    class PolParties(models.TextChoices):
        D = 'D', _('Democrat')
        R = 'R', _('Republican')
        I = 'I', _('Independent')

    name = models.CharField(max_length=100)
    jurisdiction = models.CharField(max_length=100)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    active = models.BooleanField() 
    letters_authored = []
    letters_cosigned = []

    @property
    def all_letters(self):
        return self.letters_athored + self.letters_cosigned

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
    
    class Support(models.TextChoices):
        rep = 'Republicano', _('Republican')
        dem = 'Demócrata', _('Democrat')
        bi= 'Bipartidista', _('Bipartisan')
    
    class Sentiment(models.TextChoices):
        Pos = 1, _('Positive')
        Neut = 2, _('Neutral')
        Neg = 3, _('Negative')

    class Dummy(models.TextChoices):
        y = 1, _('Yes')
        n = 0, _('No')


    topic = models.CharField(max_length=25)
    specific_topic = models.CharField(max_length=100)
    date = models.DateTimeField(help_text="Enter dates in <em>MM/DD/YYYY</em> format")
    kind_of_statement = models.CharField(max_length=15,
                                        choices=Statements.choices)
    description = models.TextField(verbose_name=_('Short Description'))
    positive_MX = models.CharField(max_length=8,
                                    choices=Sentiment.choices,
                                    verbose_name=_('Positive for Mexico?'))
    MX_mentioned = models.CharField(max_length=3,
                                    choices=Dummy.choices,
                                    verbose_name=_('Was Mexico directly mentioned?'))
    recipient = models.CharField(max_length=50, verbose_name=_('Recipient(s)'))
    chamber = models.CharField(max_length=9,
                                 choices=Chamber.choices,
                                 verbose_name=_('Letter\'s Chamber of Origin'))  
    kind_statement_party = models.CharField(max_length=12,
                                            choices=Support.choices)
    legislator = models.CharField(max_length=60,
                                 verbose_name=_('Legislator Name'),
                                 help_text=
                                 "Names are displayed in <em>Last Name, First Name</em> format")
    cosigners = models.CharField(max_length=500)
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    caucus = models.CharField(max_length=100)

    link = models.URLField("Letter URL")
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)
    comments =  models.TextField(default='N/a')
    action = models.CharField(max_length=100)
    notice_num = models.CharField(max_length=30,
                                verbose_name=_('If a notice was sent, specify the number'),
                                default='N/a')
    choices_ = [('one', 'ONE'), ('two', 'TWO')]

    @property
    def author(self):
        return self.legislator

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



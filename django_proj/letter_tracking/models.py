from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from warnings import filterwarnings
import us
filterwarnings('ignore', message=r'.*received a naive datetime')

#Meta topic models for dropdown menus and organization
class Topic(models.Model):
    topic_name = models.CharField(max_length=25)

    def __str__(self):
        return self.topic_name

class Specific_Topic(models.Model):
    specific_topic_name =  models.CharField(max_length=25)
    
    def __str__(self):
        return self.specific_topic_name

class Recipient(models.Model):
    recipient_name =  models.CharField(max_length=50)
    
    def __str__(self):
        return self.recipient_name

class Caucus(models.Model):
    caucus_name = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Caucuses"
    def __str__(self):
        return self.caucus_name

class Legislature(models.Model):
    legislature_name =  models.CharField(max_length=6)
    def __str__(self):
        return self.legislature_name

class Action(models.Model):
    action_name =  models.CharField(max_length=40)
    def __str__(self):
        return self.action_name

def zip_choices(choice_list):
    return zip(choice_list, choice_list)

#Legislator and Letter Models 
class Legislator(models.Model):

    class RepSen(models.TextChoices):
        REP = 'Rep.', _('Representative')
        SEN = 'Sen.', _('Senator')

    class PolParties(models.TextChoices):
        D = 'D', _('Democrat')
        R = 'R', _('Republican')
        I = 'I', _('Independent')

    STATES = zip_choices(list(map(lambda state: state.abbr, us.states.STATES)) + ["DC"])
    name = models.CharField(max_length=100)
    jurisdiction = models.CharField(max_length=100)
    state = models.CharField(max_length=30,
                            choices=STATES)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    active = models.BooleanField() 

    @property
    def letters_authored(self):
        authored = list(Letter.objects.filter(patrocinador=self.name).all())
        return sorted(authored, key=lambda letter: (letter.fecha, letter.consecutive_number), reverse=True)

    @property
    def letters_cosigned(self):
        cosigns = {letter:letter.cosigners.split(', ') for letter in Letter.objects.all() if letter.cosigners}
        cosigns = [letter for letter, signers in cosigns.items() if self.name in signers]
        return sorted(cosigns, key=lambda letter: (letter.fecha, letter.consecutive_number), reverse=True)
        
    @property
    def all_letters(self):
        return self.letters_authored + self.letters_cosigned

    @property
    def num_letters_authored(self):
        return len(self.letters_authored)

    @property
    def num_letters_cosigned(self):
        return len(self.letters_cosigned)
    
    @property
    def num_all_letters(self):
        return len(self.all_letters)

    def __str__(self):
        return self.name

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

    tema = models.CharField(max_length=25, choices= zip_choices(Topic.objects.all()))
    tema_específico = models.CharField(max_length=25, choices= zip_choices(Specific_Topic.objects.all()))
    fecha = models.DateTimeField(help_text="Enter dates in <em>MM/DD/YYYY</em> format")
    descripción = models.TextField(verbose_name=_('Short Description'))
    favorable_a_MX = models.CharField(max_length=8,
                                    choices=Sentiment.choices,
                                    verbose_name=_('Positive for Mexico?'))
    mención_directa_a_MX = models.IntegerField(
                                    choices=Dummy.choices,
                                    verbose_name=_('Was Mexico directly mentioned?'))
    destinatario = models.CharField(max_length=50, choices= zip_choices(Recipient.objects.all()))
    cámara = models.CharField(max_length=9,
                                 choices=Chamber.choices,
                                 verbose_name=_('Letter\'s Chamber of Origin'))  
    caucus = models.CharField(max_length=50, choices=zip_choices(Caucus.objects.all()))
    legislatura = models.CharField(max_length=50, choices=zip_choices(Legislature.objects.all()))
    patrocinador = models.CharField(max_length=60,
                                 verbose_name=_('Legislator Name'),
                                 help_text=
                                 "Names are displayed in <em>Last Name, First Name</em> format")
    cosigners = models.CharField(max_length=500)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    link = models.URLField("Letter URL")
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)
    observaciones =  models.TextField(default='N/a')
    acción = models.CharField(max_length=100, choices=zip_choices(Action.objects.all()))
    notice = models.CharField(max_length=9,
                                verbose_name=_('If a notice was sent, specify the number'),
                                default='N/a')

    @property
    def party_affiliation(self):
        return Legislator.objects.filter(name=self.patrocinador).first().party[0]

    @property 
    def cosign_sorted(self):
        return ', '.join(sorted(self.cosigners.split(', '), key=lambda lname: (lname[0], lname[1]))) if self.cosigners else 'Na'

    @property
    def author(self):
        return self.patrocinador

    @property
    def consecutive_number(self):
        daily_order = list(Letter.objects.filter(fecha=self.fecha).order_by('fecha'))
        return daily_order.index(self) + 1

    @property
    def title(self):
        return str(self.fecha)[:10].replace('-', '.') + '.' + str(self.cámara)[0] +\
                '.' + str(self.party_affiliation) + '.' + str(self.tema) + '.' + str(self.consecutive_number)
    
    @property
    def num_reps_sens(self):
        signers = (self.author + ', ' + self.cosigners).split(', ')
        #if no cosigners:
        if not signers[1]:
            sen_rep =  Legislator.objects.filter(name=signers[0]).first().rep_or_sen
            return (1, 0) if sen_rep == 'Sen.' else (0, 1)
        sen_rep = list(map(lambda name_: Legislator.objects.filter(name=name_).first().rep_or_sen, signers))
        sen = sen_rep.count('Sen.')
        rep = len(sen_rep) - sen
        return sen, rep

    @property
    def num_sens(self):
        return self.num_reps_sens[0]

    @property
    def num_reps(self):
        return self.num_reps_sens[1]

    @property
    def partido(self):
        if not self.cosigners:
            return "Demócrata" if Legislator.objects.filter(name=self.patrocinador).first().party == 'D' else "Republicano"
        signers = (self.author + ', ' + self.cosigners).split(', ')
        parties = list(map(lambda leg: Legislator.objects.filter(name=leg).first().party == 'D', signers))
        if all(parties):
            return 'Demócrata'
        if not any(parties):
            return "Republicano"
        else:
            return "Bipartidista"

    @property
    def copatrocinador(self):
        if not self.cosigners:
            return 'Na'
        def get_dist(self):
            if self.rep_or_sen == "Sen.":
                return ''
            if self.jurisdiction[-2:].isdigit():
                return '-' + jurisdiction[-2]
            elif self.jusridiction[-1].isdigit():
                return '-' + self.jusridiction[-1]
            else:
                return '-at large'
        leg_list = list(map(lambda name_: Legislator.objects.filter(name=name_).first(), self.cosigners.split(', ')))
        leg_list = list(map(lambda leg_obj: leg_obj.name + ' ' + leg_obj.party + '-' +  leg_obj.state + get_dist(leg_obj)\
                    , leg_list))
        return ', '.join(sorted(leg_list))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})



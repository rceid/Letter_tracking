from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from warnings import filterwarnings
from multiselectfield import MultiSelectField
from django import forms
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
    caucus_name = models.CharField(max_length=25, blank=True, null=True, default='Na')
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
    
def classify_letter(letter, attr, measure, options):
    if not letter.cosigners:
        return options[0] if letter.patrocinador.__dict__[attr] == measure else options[1]
    signers = [leg for leg in Legislator.objects.all() if leg.name in letter.cosigners]
    #signers = (letter.patrocinador.name + ', ' + ', '.join(letter.cosigners)).split(', ')
    classified = list(map(lambda leg_obj: leg_obj.party == 'D', signers))
    #classified = list(map(lambda leg: Legislator.objects.filter(name=leg).first().party == 'D', signers))
    if all(classified):
        return options[0]
    if not any(classified):
        return options[1]
    else:
        return options[2]

STATES = zip_choices(list(map(lambda state: state.abbr, us.states.STATES)) + ["DC"])

#Legislator and Letter Models 
class Legislator(models.Model):

    class RepSen(models.TextChoices):
        REP = 'Rep.', _('Representative')
        SEN = 'Sen.', _('Senator')

    class PolParties(models.TextChoices):
        D = 'D', _('Democrat')
        R = 'R', _('Republican')
        I = 'I', _('Independent')

    # first_name = models.CharField(max_length=100, default='None')
    # last_name = models.CharField(max_length=100, default='None')
    name = models.CharField(max_length=100, default='None')
    state = models.CharField(max_length=30,
                            choices=STATES)
    district = models.CharField(max_length=10,\
                                choices=[('N/a', '')] + list(zip_choices(['at large'] + list(map(lambda num: str(num), range(1,54))))),\
                                help_text='If politician is a Sentor, please select N/a')
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    active = models.BooleanField() 

    @property
    def title(self):
        return self.name + ' (' + self.party + '-' + self.state + '-' +  self.district +')' if self.rep_or_sen == 'Rep.'\
         else self.name + ' (' + self.party + '-' + self.state + ')'
    
    @property
    def full_title(self):
        return self.rep_or_sen + ' ' + self.title

    @property
    def letters_authored(self):
        authored = list(Letter.objects.filter(patrocinador=self).all())
        return sorted(authored, key=lambda letter: (letter.fecha, letter.consecutive_number), reverse=True)

    @property
    def letters_cosigned(self):
        cosigns = {letter:list(letter.cosigners) for letter in Letter.objects.all() if letter.cosigners}
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

    tema = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    tema_específico = models.ForeignKey(Specific_Topic, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(help_text="Enter dates in <em>MM/DD/YYYY</em> format")
    descripción = models.TextField()
    favorable_a_MX = models.CharField(max_length=8,
                                    choices=Sentiment.choices,
                                    verbose_name=_('Positive for Mexico?'))
    mención_directa_a_MX = models.CharField(max_length=3,
                                    choices=Dummy.choices,
                                    verbose_name=_('Was Mexico directly mentioned?'))
    destinatario = models.ForeignKey(Recipient, on_delete=models.SET_NULL, null=True)
    caucus = models.ForeignKey(Caucus, on_delete=models.SET_NULL, null=True)
    legislatura = models.ForeignKey(Legislature, on_delete=models.SET_NULL, null=True)
    patrocinador_sen = models.ForeignKey(Legislator, on_delete=models.SET_NULL, null=True, \
                                    verbose_name=_('Senate Author'))
    patrocinador_rep = models.CharField(max_length=100,
                                 choices=zip_choices([None] + list(Legislator.objects.filter(rep_or_sen='Sen.'))),
                                 verbose_name=_('House Author'))
    cosigners = MultiSelectField(choices=zip_choices(list(map(lambda leg: leg.name, Legislator.objects.all()))),\
                                verbose_name=_('Copatrocinador/a'), default='None')
    link = models.URLField("Letter URL")
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)
    observaciones =  models.TextField(default='N/a')
    acción = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True)
    notice = models.CharField(max_length=9,
                              verbose_name=_('If a notice was sent, specify the number'),
                              default='N/a')
    @property
    def two_authors(self):
        auths = [self.patrocinador_rep, self.patrocinador_sen]
        return True if all(auths) else False

    @property
    def partido(self):
        return classify_letter(self, 'party', "D", ['Demócrata', 'Republicano', 'Bipartidista'])

    @property
    def cámara(self):
        return classify_letter(self, 'rep_or_sen', "Sen.", ["Senado", "Cámara", "Bicameral"])

    @property 
    def cosign_sorted(self):
        return ', '.join(sorted(self.cosigners.split(', '), key=lambda lname: (lname[0], lname[1]))) if self.cosigners else 'Na'

    @property
    def consecutive_number(self):
        daily_order = list(Letter.objects.filter(fecha=self.fecha).order_by('fecha'))
        return daily_order.index(self) + 1

    @property
    def title(self):
        return str(self.fecha)[:10].replace('-', '.') + '.' + str(self.cámara)[0] +\
                '.' + str(self.patrocinador.name) + '.' + str(self.tema) + '.' + str(self.consecutive_number)

    @property
    def chamber(self):
        return None

    @property
    def num_reps_sens(self):
        signers = (self.patrocinador.name + ', ' + ', '.join(self.cosigners)).split(', ')
        #if no cosigners:
        if not signers[1]:
            sen_rep =  self.patrocinador.rep_or_sen
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
    def copatrocinador(self):
        if not self.cosigners:
            return 'Na'
        leg_list = list(map(lambda name_: Legislator.objects.filter(name=name_).first(), self.cosigners))
        leg_list = list(map(lambda leg_obj: leg_obj.title, leg_list))
        return ', '.join(sorted(leg_list))

    @property
    def letter_path(self):
         return "G:\\Cartas Legisladores\\" + str(self.legislatura) + '\\' + self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})



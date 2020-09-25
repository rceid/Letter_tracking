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
class State(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=2)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('topic_name',)
    def __str__(self):
        return self.topic_name

class Specific_Topic(models.Model):
    specific_topic_name =  models.CharField(max_length=100)
        
    class Meta:
        ordering = ('specific_topic_name',)

    def __str__(self):
        return self.specific_topic_name

class Recipient(models.Model):
    recipient_name =  models.CharField(max_length=100)
    class Meta:
        ordering = ('recipient_name',)
    def __str__(self):
        return self.recipient_name

class Caucus(models.Model):
    caucus_name = models.CharField(max_length=100, blank=True, null=True, default='Na')

    class Meta:
        verbose_name_plural = "Caucuses"
        ordering = ('caucus_name',)

    def __str__(self):
        return self.caucus_name

class Legislature(models.Model):
    legislature_name =  models.CharField(max_length=10)

    class Meta:
        ordering = ('legislature_name',)
        
    def __str__(self):
        return self.legislature_name

class Action(models.Model):
    action_name =  models.CharField(max_length=100)
    class Meta:
        ordering = ('action_name',)

    def __str__(self):
        return self.action_name

def zip_choices(choice_list):
    return zip(choice_list, choice_list)
    
def classify_letter(letter, attr, class_, options):
    if not letter.cosigners:
        if len(letter.authors) == 1: ###
            return options[0] if getattr(letter.authors[0], attr) == class_ else options[1]
        elif len(letter.authors) == 2:
            classified = list(map(lambda leg_obj: getattr(leg_obj, attr) == class_, letter.authors))
    else:
        signers = letter.authors + [leg for leg in Legislator.objects.all() if leg.name in letter.cosigners]
        classified = list(map(lambda leg_obj: leg_obj.__dict__[attr] == class_, signers))
    if all(classified):
        return options[0]
    if not any(classified):
        return options[1]
    else:
        return options[2]

def obj_list_to_attr(obj_list, attr):
    return list(map(lambda obj: getattr(obj, attr), obj_list))

#Legislator and Letter Models 
class Legislator(models.Model):

    class RepSen(models.TextChoices):
        REP = 'Rep.', _('Representative')
        SEN = 'Sen.', _('Senator')

    class PolParties(models.TextChoices):
        D = 'D', _('Democrat')
        R = 'R', _('Republican')
        I = 'I', _('Independent')

    class Meta:
        ordering = ('last_name', 'first_name')

    first_name = models.CharField(max_length=100, default='None')
    last_name = models.CharField(max_length=100, default='None')
    state = models.ForeignKey(State, 
                             on_delete=models.SET_NULL, 
                             null=True
                             )
    district = models.CharField(max_length=10,\
                                choices=[('', '-')] + list(zip_choices(['at large'] + list(map(lambda num: str(num), range(1,54))))),\
                                help_text='If politician is a Sentor, please select N/a',
                                blank=True)
    rep_or_sen = models.CharField(max_length=4,
                                 choices=RepSen.choices,
                                 verbose_name=_('Representative or Senator'))
    party = models.CharField(max_length=11, 
                            choices=PolParties.choices)
    active = models.BooleanField()

    @property
    def name(self):
        return self.last_name + ' ' + self.first_name

    @property
    def title(self):
        return self.name + ' (' + self.party + '-' + self.state.abbr + '-' +  self.district +')' if self.rep_or_sen == 'Rep.'\
         else self.name + ' (' + self.party + '-' + self.state.abbr + ')'
    
    @property
    def full_title(self):
        return self.rep_or_sen + ' ' + self.title

    @property
    def letters_authored(self):
        authored = list(Letter.objects.filter(patrocinador_sen=self) | Letter.objects.filter(patrocinador_rep=self))
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
        rep = 'Republican', _('Republican')
        dem = 'Democrat', _('Democrat')
        bi= 'Bipartisan', _('Bipartisan')
    
    class Sentiment(models.TextChoices):
        Pos = 'Positive', _('Positive')
        Neut = 'Neutral', _('Neutral')
        Neg = 'Negative', _('Negative')

    class Dummy(models.TextChoices):
        y = 1, _('Yes')
        n = 0, _('No')

    class Meta:
        ordering = ('fecha', )

    tema = models.ForeignKey(Topic, 
                            on_delete=models.SET_NULL, 
                            null=True,
                            verbose_name=_('Topic')
                            )
    tema_específico = models.ForeignKey(Specific_Topic, 
                                        on_delete=models.SET_NULL, 
                                        null=True,
                                        verbose_name=_('Specific Topic')
                                        )
    fecha = models.DateTimeField(help_text="Enter dates in <em>MM/DD/YYYY</em> format", verbose_name=_('Date'))
    descripción = models.TextField(verbose_name=_('Description'))
    favorable_a_MX = models.CharField(max_length=8,
                                    choices=Sentiment.choices,
                                    verbose_name=_('Positive for Mexico?')
                                    )
    mención_directa_a_MX = models.CharField(max_length=3,
                                    choices=Dummy.choices,
                                    verbose_name=_('Was Mexico directly mentioned?'))
    destinatario = MultiSelectField(choices=[('N/a', 'N/a')] + list(zip_choices(list(map(lambda obj: obj.recipient_name, Recipient.objects.all())))),
                                default='None',
                                max_length=100,
                                help_text="<em>If 'Other', please specify in the text box below</em>",
                                verbose_name=_('Recipients')
                                )
    other_destinatario_comments = models.TextField(blank=True,
                                                   verbose_name=_('Other recipient comments'))
    caucus = MultiSelectField(choices=[('', 'N/a')] + list(zip_choices(list(map(lambda obj: obj.caucus_name, Caucus.objects.all())))),
                                default='N/a',
                                max_length=100
                                )
    legislatura = models.ForeignKey(Legislature, 
                                    on_delete=models.SET_NULL, 
                                    null=True,
                                    verbose_name=_('Legislature')
                                    )
    patrocinador_sen = models.ForeignKey(Legislator, 
                                        limit_choices_to={'rep_or_sen': 'Sen.', 'active': True}, 
                                        related_name='Senators',
                                        verbose_name=_('Senate Author'), 
                                        on_delete=models.SET_NULL, 
                                        null=True,
                                        blank=True
                                        )
    patrocinador_rep = models.ForeignKey(Legislator, 
                                        limit_choices_to={'rep_or_sen': 'Rep.', 'active': True}, 
                                        related_name='Representatives',
                                        verbose_name=_('House Author'), 
                                        on_delete=models.SET_NULL, 
                                        null=True,
                                        blank=True
                                        )
    cosigners = MultiSelectField(choices=[('', 'N/a')] + list(zip_choices(list(map(lambda leg: leg.name, Legislator.objects.filter(active=True))))),\
                                verbose_name=_('Cosigner(s)'), 
                                default='None',
                                max_length=1000
                                )
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, 
                                 null=True
                                 )
    observaciones =  models.TextField(default='N/a',
                                      verbose_name=_('Comments')
                                      )
    acción = models.ForeignKey(Action,
                               on_delete=models.SET_NULL, 
                               null=True,
                               verbose_name=_('Action')
                               )
    notice = models.CharField(max_length=9,
                              verbose_name=_('If a notice was sent, specify the number'),
                              default='N/a'
                              )
    letter_path = models.CharField(max_length=200,
                                   verbose_name=_('File Path'),
                                   help_text="For example, 'G:\\Cartas Legisladores\\116th\\2019.01.23.S.Casey.Migration.1'",
                                   blank=True)

    @property
    def title(self):
        if not self.authors:
            name = 'NO LEGISLATOR SELECTED: UPDATE LETTER'
        else:
            name = '-'.join(obj_list_to_attr(self.authors, 'last_name'))
        return '.'.join([str(self.fecha)[:10].replace('-', '.'), self.cámara[0],\
               self.partido[0], name, str(self.tema), str(self.consecutive_number)])

    @property
    def authors(self):
        auths = [leg for leg in [self.patrocinador_rep, self.patrocinador_sen] if leg]
        return auths if auths else []

    @property
    def two_authors(self):
        return True if len(self.authors) == 2 else False

    @property
    def sen_author(self):
        return True if self.patrocinador_sen else False

    @property
    def rep_author(self):
        return True if self.patrocinador_rep else False

    @property
    def partido(self):
        return classify_letter(self, 'party', "D", ['Democrat', 'Republican', 'Bipartisan'])

    @property
    def cámara(self):
        return classify_letter(self, 'rep_or_sen', "Sen.", ["Senate", "House", "Bicameral"])

    @property 
    def cosign_sorted(self):
        return ', '.join(sorted(self.cosigners)) if self.cosigners else 'N/a'
    @property
    def date(self):
        return self.fecha.date()
    @property
    def consecutive_number(self):
        daily_order = list(Letter.objects.filter(fecha=self.fecha).order_by('fecha'))
        return daily_order.index(self) + 1

    @property
    def num_reps_sens(self):
        if not self.authors:
            return 0, 0
        auths = obj_list_to_attr(self.authors, 'name') #list of name strings
        signers = auths + ', '.join(self.cosigners).split(', ') #larger list of name strings
        #if no cosigners:
        if not self.cosigners:
            sen_rep = obj_list_to_attr(self.authors, 'rep_or_sen')
            if len(sen_rep) == 1:
                return (1, 0) if sen_rep == ['Sen.'] else (0, 1)
            elif len(sen_rep) == 2:
                return sen_rep.count('Sen.'), sen_rep.count('Rep.')
        sen_rep = [leg.rep_or_sen for leg in Legislator.objects.all() if leg.name in signers]

        return sen_rep.count('Sen.'), sen_rep.count('Rep.')

    @property
    def num_sens(self):
        return self.num_reps_sens[0]

    @property
    def num_reps(self):
        return self.num_reps_sens[1]

    @property
    def copatrocinador(self):
        if not self.cosigners:
            return 'N/a'
        leg_list = [cosigner for cosigner in Legislator.objects.all() if cosigner.name in self.cosigners]
        leg_list = sorted(leg_list, key=lambda leg: (leg.rep_or_sen, leg.name))
        leg_list = list(map(lambda leg_obj: leg_obj.full_title, leg_list))
        return ', '.join(sorted(leg_list))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('letter-detail', kwargs={'pk':self.pk})



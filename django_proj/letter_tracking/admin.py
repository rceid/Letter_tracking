from django.contrib import admin
from django.contrib.admin import SimpleListFilter, ModelAdmin
from .list_filters import StateListFilter, ActiveListFilter, PartyListFilter, RepSenListFilter
from .models import (Letter,
                    Legislator,
                    Topic,
                    Specific_Topic,
                    Recipient,
                    Caucus,
                    Legislature,
                    Action)

# admin.site.register(Letter)
admin.site.register(Topic)
admin.site.register(Specific_Topic)
admin.site.register(Recipient)
admin.site.register(Caucus)
admin.site.register(Legislature)
admin.site.register(Action)

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'tema', 'tema_específico','fecha', 'favorable_a_MX', 'mención_directa_a_MX', 'destinatario', 'cámara',
                    'partido', 'caucus', 'legislatura', 'patrocinador_sen', 'patrocinador_rep', 'acción', 'notice')
    list_filter = ('legislatura','acción', 'caucus', 'tema', 'tema_específico', 'destinatario',  )

@admin.register(Legislator)
class LegAdmin(admin.ModelAdmin):
    list_display = ('name','state', 'district', 'party', 'rep_or_sen', 'num_all_letters', 'letters_authored' )
    list_filter = (ActiveListFilter, PartyListFilter, RepSenListFilter, StateListFilter, )

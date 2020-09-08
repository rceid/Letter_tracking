from django.contrib import admin
from django.contrib.admin import SimpleListFilter, ModelAdmin
from django.http import HttpResponse
from .views import LEG_ATTRS
import csv
from .list_filters import (ActiveListFilter, 
                           PartyListFilter, 
                           RepSenListFilter,
                           StateLetterFilter,
                           ExportCsv)
from .models import (Letter,
                    Legislator,
                    Topic,
                    Specific_Topic,
                    Recipient,
                    Caucus,
                    Legislature,
                    Action,
                    State)

admin.site.register(Topic)
admin.site.register(Specific_Topic)
admin.site.register(Recipient)
admin.site.register(Caucus)
admin.site.register(Legislature)
admin.site.register(Action)
admin.site.register(State)


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin, ExportCsv):
    list_display = ('title', 'tema', 'tema_específico','date', 'descripción', 'favorable_a_MX', 'mención_directa_a_MX', 
                    'destinatario', 'cámara', 'partido', 'caucus', 'legislatura', 'num_reps', 'num_sens', 
                    'patrocinador_sen', 'patrocinador_rep', 'cosign_sorted', 'letter_path', 'observaciones', 'acción', 'notice')
    list_filter = ('legislatura','acción', 'caucus', 'tema', 'tema_específico', 'destinatario', StateLetterFilter)
    actions = ["export_as_csv"]

@admin.register(Legislator)
class LegAdmin(admin.ModelAdmin, ExportCsv):
    list_display = LEG_ATTRS
    list_filter = (ActiveListFilter, PartyListFilter, RepSenListFilter, 'state', )
    actions = ["export_as_csv"]

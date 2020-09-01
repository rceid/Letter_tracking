from django.contrib import admin
from django.contrib.admin import SimpleListFilter, ModelAdmin
from django.http import HttpResponse
from .views import get_letter_values, lookup_attr, EXPORT_ATTRS
import csv
from .list_filters import StateListFilter, ActiveListFilter, PartyListFilter, RepSenListFilter
from .models import (Letter,
                    Legislator,
                    Topic,
                    Specific_Topic,
                    Recipient,
                    Caucus,
                    Legislature,
                    Action)

admin.site.register(Topic)
admin.site.register(Specific_Topic)
admin.site.register(Recipient)
admin.site.register(Caucus)
admin.site.register(Legislature)
admin.site.register(Action)

class ExportCsvLetter:
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow(EXPORT_ATTRS)
        for obj in queryset:
            authors = ['', '']
            if obj.sen_author:
                authors[0] = obj.patrocinador_sen.name
            if obj.rep_author:
                authors[1] = obj.patrocinador_rep.name
            tema, tema_específico, destinatario, caucus, legislatura, senadores, congresistas, acción = get_letter_values(obj)
            vals = [obj.title, tema, tema_específico, obj.fecha, obj.descripción, obj.favorable_a_MX, obj.mención_directa_a_MX,
                    obj.destinatario, obj.cámara, obj.partido, caucus, legislatura, congresistas, senadores, obj.cosign_sorted, 
                    obj.letter_path, obj.observaciones, acción, obj.notice]
            vals.insert(14, authors[0])
            vals.insert(15, authors[1])
            print('VALUES:\n',vals)
            writer.writerow(vals)
        response['Content-Disposition'] = 'attachment; filename="letters.csv"'

        return response
    export_as_csv.short_description = "Export Selected"

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin, ExportCsvLetter):
    list_display = ('title', 'tema', 'tema_específico','fecha', 'descripción', 'favorable_a_MX', 'mención_directa_a_MX', 
                    'destinatario', 'cámara', 'partido', 'caucus', 'legislatura', 'num_reps', 'num_sens', 
                    'patrocinador_sen', 'patrocinador_rep', 'cosign_sorted', 'letter_path', 'observaciones', 'acción', 'notice')
    list_filter = ('legislatura','acción', 'caucus', 'tema', 'tema_específico', 'destinatario' )
    actions = ["export_as_csv"]

@admin.register(Legislator)
class LegAdmin(admin.ModelAdmin):
    list_display = ('name','state', 'district', 'party', 'rep_or_sen', 'num_all_letters', 'letters_authored' )
    list_filter = (ActiveListFilter, PartyListFilter, RepSenListFilter, StateListFilter, )
    actions = ["export_as_csv"]

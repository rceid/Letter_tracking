from django.contrib import admin
from .models import Legislator, Letter, Topic, State
from .views import get_letter_values, EXPORT_ATTRS, LEG_ATTRS
from django.db.models import Q


class StateLetterFilter(admin.SimpleListFilter):
    title = 'State'
    parameter_name = 'state_letter'
    default_value = None

    def lookups(self, request, model_admin):
         
        return [(state_obj.id, state_obj.abbr) for state_obj in State.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            leg_id = list(map( lambda leg: leg.id, Legislator.objects.filter(state=self.value())))
            rv = queryset.filter(patrocinador_sen_id__in=leg_id) | queryset.filter(patrocinador_rep_id__in=leg_id)
            return rv
            
        return queryset

class PartyListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Party'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'party'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        
        return (("D", "Democrat"), ("R", "Republican"))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(party=self.value())
        return queryset

class RepSenListFilter(admin.SimpleListFilter):

    title = 'Rep or Sen'
    parameter_name = 'reporsen'

    default_value = None

    def lookups(self, request, model_admin):

        return (("Sen.", "Senator"), ("Rep.", "Representative"))

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(rep_or_sen=self.value())
        return queryset

class ActiveListFilter(admin.SimpleListFilter):

    title = 'Active'
    parameter_name = 'active'
    default_value = None

    def lookups(self, request, model_admin):

        return ((True, 'Active'), (False, 'Inactive'))

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(active=self.value())
        return queryset
        
class ExportCsv:
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        if isinstance(queryset[0], Legislator):
            writer.writerow(LEG_ATTRS)
            for leg in queryset:
                vals = [getattr(leg, field) for field in LEG_ATTRS]
                vals[LEG_ATTRS.index('letters_authored')] = ', '.join([letter.title for letter in leg.letters_authored])
                row = writer.writerow(vals)
            response['Content-Disposition'] = 'attachment; filename="legislators.csv"'

            return response
        elif isinstance(queryset[0], Letter):
            writer.writerow(EXPORT_ATTRS)
            for obj in queryset:
                authors = ['', '']
                if obj.sen_author:
                    authors[0] = obj.patrocinador_sen.name
                if obj.rep_author:
                    authors[1] = obj.patrocinador_rep.name
                tema, tema_específico, destinatario, caucus, legislatura, senadores, congresistas, acción = get_letter_values(obj)
                vals = [obj.title, tema, tema_específico, obj.fecha.date(), obj.descripción, obj.favorable_a_MX, obj.mención_directa_a_MX,
                        obj.destinatario, obj.cámara, obj.partido, caucus, legislatura, congresistas, senadores, obj.cosign_sorted, 
                        obj.letter_path, obj.observaciones, acción, obj.notice]
                vals.insert(14, authors[0])
                vals.insert(15, authors[1])
                writer.writerow(vals)
            response['Content-Disposition'] = 'attachment; filename="letters.csv"'

            return response
    export_as_csv.short_description = "Export Selected"
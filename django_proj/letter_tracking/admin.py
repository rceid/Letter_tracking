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

admin.site.register(Letter)
admin.site.register(Topic)
admin.site.register(Specific_Topic)
admin.site.register(Recipient)
admin.site.register(Caucus)
admin.site.register(Legislature)
admin.site.register(Action)

@admin.register(Legislator)
class LegAdmin(admin.ModelAdmin):
    list_display = ('name','state', 'district', 'party', 'rep_or_sen' )
    list_filter = (ActiveListFilter, PartyListFilter, StateListFilter,RepSenListFilter  )

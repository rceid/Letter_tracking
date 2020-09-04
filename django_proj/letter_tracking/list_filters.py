from django.contrib import admin
from .models import Legislator, Letter, Topic
import us

def zip_options(options):
    return tuple(zip(options, options))


class TopicListFilter(admin.SimpleListFilter):
    title = 'Topic'
    parameter_name = 'topic'
    default_value = None

    def lookups(self, request, model_admin):
        return None
    def queryset(self, request, queryset):
        return None
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

class ActiveListFilter(admin.SimpleListFilter):

    title = 'Active'

    parameter_name = 'active'

    default_value = None

    def lookups(self, request, model_admin):

        active_or_not = (True, False)
        return zip_options(active_or_not)

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(active=self.value())
        return queryset

class StateListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    title = 'state'

    parameter_name = 'state'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        states = sorted(list(map(lambda state: state.abbr, us.states.STATES)) + ["DC"])
        
        return zip_options(states)

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(state=self.value())
        return queryset

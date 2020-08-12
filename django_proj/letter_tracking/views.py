from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView,
                                 TemplateView)
from .models import Letter, Legislator
from django.db.models import Q

FIELDS = ['topic', 'legislator', 'party','rep_or_sen','cosigners',
             'description', 'date', 'caucus', 'chamber', 'link', 'specific_topic',
             'kind_of_statement', 'positive_MX', 'MX_mentioned', 'recipient', 
             'kind_statement_party', 'comments', 'action', 'notice_num'
             ]

def home(request):
    context ={
        'letters': Letter.objects.all()
    }
    return render(request, 'letter_tracking/home.html', context)

class LetterListView(ListView):
    model = Letter
    template_name = 'letter_tracking/home.html'
    context_object_name = 'letters'
    ordering = ['-date', '-date_posted']
    paginate_by = 15

class LegLetterView(ListView):
    model = Legislator 
    template_name = 'letter_tracking/legislator_letters.html'
    context_object_name = 'politician'
    
    def get_queryset(self):
        return get_object_or_404(Legislator, name=self.kwargs.get('name'))

class UserLetterListView(ListView):
    model = Letter
    template_name = 'letter_tracking/legislator_letters.html'
    context_object_name = 'letters'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Letter.objects.filter(posted_by_id=user).order_by('-date_posted')

class LetterDetailView(DetailView):
    model = Letter

class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Letter
    fields = FIELDS

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class LetterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Letter
    fields = FIELDS

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True
        # letter = self.get_object()
        # if self.request.user == letter.posted_by:
        #     return True
        # return False

class LetterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Letter
    success_url = '/'

    def test_func(self):
        return True
        # letter = self.get_object()
        # if self.request.user == letter.posted_by:
        #     return True
        # return False

class SearchFormView(TemplateView):
    template_name = 'letter_tracking/search_form.html'

class SearchResultsView(ListView):
    model = Legislator
    template_name = 'letter_tracking/search_results.html'
    context_object_name = 'politician'
    #paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        return get_object_or_404(Legislator, name__icontains=query)


def about(request):
    return render(request, 'letter_tracking/about.html', {'title': 'About'})

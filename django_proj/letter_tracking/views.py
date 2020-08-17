from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.views.generic import (ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView,
                                 TemplateView)
from .models import Letter, Legislator
from django.db.models import Q
import csv, io

FIELDS = ['tema', 'patrocinador','rep_or_sen','cosigners',
             'descripción', 'fecha', 'caucus', 'cámara', 'link', 'tema_específico',
             'favorable_a_MX', 'mención_directa_a_MX', 'destinatario', 
             'observaciones', 'acción', 'notice'
             ]


def about(request):
    return render(request, 'letter_tracking/about.html', {'title': 'About'})

def home(request):
    context ={
        'letters': Letter.objects.all()
    }
    return render(request, 'letter_tracking/home.html', context)

class LetterListView(ListView):
    model = Letter
    template_name = 'letter_tracking/home.html'
    context_object_name = 'letters'
    ordering = ['-fecha', '-date_posted']
    paginate_by = 15
    
class LegLetterView(ListView):
    model = Legislator 
    template_name = 'letter_tracking/legislator_letters.html'
    context_object_name = 'politician'
    #paginate_by = 5

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

    def get_queryset(self):
        query = self.request.GET.get('q')
        return get_object_or_404(Legislator, name__icontains=query)


def export(self, name=None):
    attrs= list(Letter.objects.first().__dict__.keys())[2:] 
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['Código'] + attrs + ['State', 'Senadores', 'Congresistas', 'Partido'])
    if not name:
        letters = Letter.objects.all()
    else:
        letters = Legislator.objects.filter(name=name).first().all_letters
    for letter in letters:
        num_sen, num_rep = letter.num_reps_sens
        vals = [letter.title] + list(letter.__dict__.values())[2:] + \
                [Legislator.objects.filter(name=letter.patrocinador).first().state,\
                num_sen, num_rep, letter.partido]
        writer.writerow(vals)
    
    response['Content-Disposition'] = 'attachment; filename="letters.csv"'

    return response

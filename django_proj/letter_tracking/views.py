from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.generic import (ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView,
                                 TemplateView)
from .models import (Letter, Legislator, 
                    Topic, Specific_Topic, 
                    Recipient, Caucus, 
                    Legislature, Action)
from django.db.models import Q
from .forms import LegSearchForm
import csv, io

FIELDS = ['tema', 'patrocinador', 'cosigners', 'descripción', 
         'fecha', 'caucus', 'legislatura', 'cámara', 'link', 'tema_específico',
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

# class SearchFormView(TemplateView):
#     template_name = 'letter_tracking/search_form.html'

def get_name(request):
    print('here')
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        print('here get')
        # create a form instance and populate it with data from the request:
        form = LegSearchForm(request.POST)
        print('form', form)
        # check whether it's valid:
        if form.is_valid():
            print('form valid')
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        else:
            print('here form')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('HERE ELSE')
        form = LegSearchForm()

    return render(request, 'letter_tracking/search_form.html', {'form': form})

class SearchResultsView(ListView):
    model = Legislator
    template_name = 'letter_tracking/search_results.html'
    context_object_name = 'politician'

    def get_queryset(self):
        query = self.request.GET.get('q')
        print('HERE', query)
        return get_object_or_404(Legislator, name__icontains=query)


def export(self, name=None):
    attrs = ['Código', 'Tema', 'Tema específico', 'Fecha', 'Descripción', 'Favorable a MX', 'Mención directa a MX', 
            'Destinatario',  'Cámara', 'Partido', 'Caucus', 'Legislatura', 'Congresistas', 'Senadores',
            'Patrocinador/a', 'Copatrocinador/a', 'Link', 'Observaciones', 'Acción', 'Notice']
    #zip rows and the attrs into a dict in the loop
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(attrs)
    if not name:
        letters = Letter.objects.all()
    else:
        letters = Legislator.objects.filter(name=name).first().all_letters
    for letter in letters:
        tema, tema_específico, destinatario, caucus, legislatura, senadores, congresistas, acción = get_letter_values(letter)
        vals = [letter.title, tema, tema_específico, letter.fecha, letter.descripción, letter.favorable_a_MX, letter.mención_directa_a_MX,
                letter.destinatario, letter.cámara, letter.partido, caucus, legislatura, congresistas, senadores, letter.patrocinador.name,
                letter.cosign_sorted, letter.letter_path, letter.observaciones, acción, letter.notice]
        writer.writerow(vals)
    
    response['Content-Disposition'] = 'attachment; filename="letters.csv"'

    return response
def get_letter_values(letter):
    tema = lookup_attr(Topic, letter.tema_id, 'topic_name')
    tema_específico = lookup_attr(Specific_Topic, letter.tema_específico_id, 'specific_topic_name')
    destinatario = lookup_attr(Recipient, letter.destinatario_id, 'recipient_name')
    caucus = lookup_attr(Caucus, letter.caucus_id, 'caucus_name')
    legislatura = lookup_attr(Legislature, letter.legislatura_id, 'legislature_name')
    senadores, congresistas = letter.num_reps_sens
    acción = lookup_attr(Action, letter.acción_id, 'action_name')

    return tema, tema_específico, destinatario, caucus, legislatura, senadores, congresistas, acción

def lookup_attr(obj, id_, attr):
    obj
    try:
        rv = obj.objects.filter(id=id_).first().__dict__[attr]
    except:
        rv = None
    return rv


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                 DetailView,
                                 CreateView,
                                 UpdateView,
                                 DeleteView)
from .models import Letter


def home(request):
    context ={
        'letters': Letter.objects.all()
    }
    return render(request, 'letter_tracking/home.html', context)

class LetterListView(ListView):
    model = Letter
    template_name = 'letter_tracking/home.html'
    context_object_name = 'letters'
    ordering = ['-date']
    paginate_by = 5

class UserLetterListView(ListView): #can adapt this to use for politicians. Video 11 pagination
    model = Letter
    template_name = 'letter_tracking/user_letters.html'
    context_object_name = 'letters'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Letter.objects.filter(posted_by_id=user).order_by('-date_posted')

class LetterDetailView(DetailView):
    model = Letter

class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Letter
    fields = ['title', 'description', 'date']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class LetterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Letter
    fields = ['title', 'description', 'date']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        letter = self.get_object()
        if self.request.user == letter.posted_by:
            return True
        return False

class LetterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Letter
    success_url = '/'

    def test_func(self):
        letter = self.get_object()
        if self.request.user == letter.posted_by:
            return True
        return False

def about(request):
    return render(request, 'letter_tracking/about.html', {'title': 'About'})

from django.urls import path
from .views import (LetterListView, 
                LetterDetailView,
                LetterCreateView,
                LetterUpdateView,
                LetterDeleteView,
                UserLetterListView,
                SearchFormView,
                SearchResultsView,
                LegLetterView
                )
from . import views

urlpatterns = [
    path('', LetterListView.as_view(), name='letter_tracking-home'),
    path('user/<str:username>/', UserLetterListView.as_view(), name='userletters'),
    path('legislator_letters/<str:name>', LegLetterView.as_view(), name='legislator-letters'),
    path('letter/int:<pk>/', LetterDetailView.as_view(), name='letter-detail'),
    path('letter/new/', LetterCreateView.as_view(), name='letter-create'),
    path('letter/int:<pk>/update/', LetterUpdateView.as_view(), name='letter-update'),
    path('letter/int:<pk>/delete/', LetterDeleteView.as_view(), name='letter-delete'),
    path('search_result/', SearchResultsView.as_view(), name='search_results'),
    path('search/', SearchFormView.as_view(), name='search_form'),
    path('about/', views.about, name='letter_tracking-about'),
    path('export/', views.export, name='export-data'),
    path('export/<str:name>/', views.export, name='export-data-leg')
]

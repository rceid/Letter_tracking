from django.urls import path
from .views import (LetterListView, 
                LetterDetailView,
                LetterCreateView,
                LetterUpdateView,
                LetterDeleteView,
                UserLetterListView)
from . import views

urlpatterns = [
    path('', LetterListView.as_view(), name='letter_tracking-home'),
    path('user/<str:username>/', UserLetterListView.as_view(), name='userletters'),
    path('letter/int:<pk>/', LetterDetailView.as_view(), name='letter-detail'),
    path('letter/new/', LetterCreateView.as_view(), name='letter-create'),
    path('letter/int:<pk>/update/', LetterUpdateView.as_view(), name='letter-update'),
    path('letter/int:<pk>/delete/', LetterDeleteView.as_view(), name='letter-delete'),
    path('about/', views.about, name='letter_tracking-about'),
]

# elections/admin_urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('candidate/', views.candidate_list, name='candidate_list'),
    path('candidate/new/', views.candidate_create, name='candidate_create'),
    path('candidate/<int:pk>/edit/', views.candidate_update, name='candidate_update'),
    path('candidate/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),
]

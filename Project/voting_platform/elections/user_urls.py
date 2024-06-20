from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_candidate_list, name='user_candidate_list'),
    path('vote/<int:pk>/', views.vote, name='vote'),
]


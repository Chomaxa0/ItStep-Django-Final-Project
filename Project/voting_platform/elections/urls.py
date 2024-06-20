from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin_panel/', include('elections.admin_urls')),
    path('vote/', include('elections.user_urls')),
    path('accounts/login/', views.custom_login_view, name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='homepage'), name='logout'),
]

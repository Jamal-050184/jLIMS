from django.urls import path
from django.contrib.auth import views
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.user_login, name='login'),
    path('base/',views.base, name='Base Page'),
    path('library/', views.librarypage, name='librarypage'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.sign_up, name='Registration'),

]   
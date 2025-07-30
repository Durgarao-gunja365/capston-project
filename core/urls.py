from django.urls import path
from . import views
from .views import empty_favicon

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
path('favicon.ico', empty_favicon),

]



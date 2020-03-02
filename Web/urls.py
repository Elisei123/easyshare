from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<name_profile>', views.name_profile_function, name='name_profile'),
]
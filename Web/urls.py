from django.urls import path

from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('error_404', views.error_404_view, name='error_404'),
    path('profile/<name_profile>', views.name_profile_function, name='name_profile'),
]
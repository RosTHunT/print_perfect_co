from django.urls import path

from . import views

app_name = 'app_profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),

]
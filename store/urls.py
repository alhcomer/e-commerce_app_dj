from django.urls import path

from . import views

app_name='store'

urlpatterns = ['', views.all_products]
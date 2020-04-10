from django.urls import path
from .views import about_page, contact_page

urlpatterns = [
    path('index/', index, name='index'),

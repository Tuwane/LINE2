from django.urls import path
from . import views

app_name = 'showmedia'

urlpatterns = [
    path('photos/', views.photos_view, name='photos')
]

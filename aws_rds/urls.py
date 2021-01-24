from django.urls import path
from . import views


urlpatterns = [
    path('createdb/', views.create_db, name='createdb'),
    path('getdbs/', views.get_db_instances, name='get_db_instances')
]
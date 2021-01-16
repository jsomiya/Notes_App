from django.urls import path
from . import views

urlpatterns = [
    path('details/<slug>/', views.details, name = 'details'),
    path('create/', views.create, name = 'create'),
    path('title_list/', views.title_list, name = 'title_list'),
    path('update_note/<slug>/', views.update_note, name = 'update_note'),
    path('delete_note/<slug>/', views.delete_note, name = 'delete_note'),
]

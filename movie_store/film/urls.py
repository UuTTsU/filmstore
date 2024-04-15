from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilmListView.as_view(), name = 'film_list' ),
    path('create', views.FilmCreateView.as_view(), name='create_film'),
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film_details'),
    path('delete/<int:pk>/', views.FilmDeleteView.as_view(), name='delete_films'),
]
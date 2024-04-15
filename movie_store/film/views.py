from django.views import generic
from .models import Film
from django.urls import reverse_lazy

class FilmListView(generic.ListView):
    model = Film

class FilmDetailView(generic.DetailView):
    model = Film

class FilmCreateView(generic.CreateView):
    model = Film
    fields = "__all__"
    success_url = reverse_lazy('film_list')

class FilmDeleteView(generic.DeleteView):
    model = Film
    success_url = reverse_lazy('film_list')






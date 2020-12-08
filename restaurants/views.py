from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from restaurants.forms import RestaurantCreateForm
from restaurants.models import Restaurants


class RestaurantsListView(ListView):
    template_name = 'restaurants/restaurants-list.html'
    model = Restaurants
    context_object_name = 'restaurants'
    paginate_by = 3

    def dispatch(self, request, *args,
                 **kwargs):
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Restaurants list'
        return context



class RestaurantsCreateView(CreateView):
    model = Restaurants
    fields = '__all__'
    template_name = 'restaurants/restaurants-create.html'
    success_url = reverse_lazy('restaurants list')


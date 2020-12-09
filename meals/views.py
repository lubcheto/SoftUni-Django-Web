from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from meals.models import RestaurantMeals


class MealsListView(ListView):
    template_name = 'meals/meals-list.html'
    model = RestaurantMeals
    context_object_name = 'meals'
    paginate_by = 6

    def dispatch(self, request, *args,
                 **kwargs):
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Meals list'
        return context


class MealsCreateView(CreateView):
    model = RestaurantMeals
    fields = ['meal_name','type','price','picture']
    template_name = 'meals/meals-create.html'
    success_url = reverse_lazy('meals list')

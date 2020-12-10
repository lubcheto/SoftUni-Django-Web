from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from meals.models import RestaurantMeals
from restaurants.models import Restaurants


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


class MealsCreateView(LoginRequiredMixin,CreateView):
    model = RestaurantMeals
    fields = ['meal_name', 'type', 'price', 'picture']
    template_name = 'meals/meals-create.html'

    def get_success_url(self):
        return reverse_lazy('restaurants details', kwargs={'pk': self.request.user.userprofile.pk})

    def form_valid(self, form):
        restaurant_user = self.request.user.userprofile.pk
        form.instance.creator_id = restaurant_user
        return super(MealsCreateView, self).form_valid(form)


class MealEditView(LoginRequiredMixin, UpdateView):
    model = RestaurantMeals
    fields = ['meal_name', 'type', 'price', 'picture']
    template_name = 'meals/meals-details.html'

    def get_success_url(self):
            return reverse_lazy('restaurants details', kwargs={'pk': self.object.creator_id})


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = RestaurantMeals
    template_name = 'meals/meals-delete.html'

    def get_success_url(self):
        return reverse_lazy('restaurants details', kwargs={'pk': self.object.creator_id})

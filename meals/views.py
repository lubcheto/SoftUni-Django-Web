from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import random
from meals.filters import FilterMeals
from meals.models import RestaurantMeals


def is_restaurant_and_auth_check(req):
    if req.user.is_authenticated and req.user.userprofile.is_restaurant:
        is_restaurant = True
    else:
        is_restaurant = False
    return is_restaurant



class MealsListView(ListView):
    template_name = 'meals/meals-list.html'
    model = RestaurantMeals
    context_object_name = 'meals'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading_text'] = 'Meals list'
        context['current_user'] = self.request.user.id
        context['queryset'] = self.queryset

        if self.request.user.is_authenticated:
            context['is_restaurant'] = self.request.user.userprofile.is_restaurant
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(meal_name__icontains=query).filter(is_eatable=True).order_by('-timestamp')
        else:
            object_list = self.model.objects.all().filter(is_eatable=True).order_by('-timestamp')
        return object_list


class MealsCreateView(LoginRequiredMixin, CreateView):
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


def browse_meals_view(request):
    all_meals = RestaurantMeals.objects.filter(is_eatable=True)
    filter_lib = FilterMeals(request.GET, queryset=all_meals)
    all_meals = filter_lib.qs
    if request.user.is_authenticated and request.user.userprofile.is_restaurant:
        is_restaurant = True
    else:
        is_restaurant = False

    context = {
        'all_meals': all_meals,
        'filter_lib': filter_lib,
        'is_restaurant': is_restaurant,
    }

    return render(request, 'meals/meals-list-browse.html', context)


def surprise_meal_view(request):
    all_meals = RestaurantMeals.objects.filter(is_eatable=True)
    random_meal = random.choice(all_meals)
    is_restaurant = is_restaurant_and_auth_check(request)
    context = {
        'random_meal':random_meal,
        'is_restaurant':is_restaurant
    }

    return render(request,'meals/surprise.html', context)


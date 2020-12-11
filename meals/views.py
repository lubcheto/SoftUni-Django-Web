from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from meals.filters import FilterMeals
from meals.models import RestaurantMeals


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
            object_list = self.model.objects.filter(meal_name__icontains=query).order_by('-timestamp')
        else:
            object_list = self.model.objects.all().order_by('-timestamp')
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

    all_meals = RestaurantMeals.objects.all()
    # filter_lib = FilterMeals(queryset=all_meals)
    # all_meals=filter_lib.qs

    context = {
        'all_meals':all_meals,
        'a':444,
    }

    return render(request, 'meals/meals-list-browse.html', context)







# def FilterForm(request):
#     meal_name = request.GET.get('meal_name')
#     type = request.GET.get('type')
#     price = request.GET.get('price')
#     meal_type = request.GET.get('')
#
#
#     Breakfast = 'breakfast'
#     Lunch = 'lunch'
#     Dinner = 'dinner'
#     Dessert = 'dessert'
#
#     MEAL_TYPES = (
#         (Breakfast, 'breakfast'),
#         (Lunch, 'lunch'),
#         (Dinner, 'dinner'),
#         (Dessert, 'dessert')
#     )

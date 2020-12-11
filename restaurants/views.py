# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RestaurantEditForm
from accounts.models import UserProfile
from meals.models import RestaurantMeals
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
    fields = ['restaurant_name', 'description','profile_picture']
    template_name = 'restaurants/restaurants-create.html'

    def get_success_url(self):
        return reverse_lazy('restaurants details', kwargs={'pk': self.request.user.userprofile.pk})


class RestaurantsDetailsView(DetailView):
    model = Restaurants
    template_name = 'restaurants/restaurants-details.html'
    context_object_name = 'restaurant'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = (self.request.user.id == self.object.user_id)
        context['can_delete'] = (self.request.user.id == self.object.user_id)
        context['owner'] = (self.request.user.id == self.object.user_id)
        context['created_meals'] = self.object.restaurants.restaurantmeals_set.all()

        if self.request.user.is_authenticated:
            context['is_restaurant'] = self.request.user.userprofile.is_restaurant
        return context




class RestaurantEditView(LoginRequiredMixin,UpdateView):
    model = Restaurants
    form_class = RestaurantEditForm
    template_name = 'restaurants/restaurants-edit.html'


    def get_success_url(self):
        return reverse_lazy('restaurants details', kwargs={'pk': self.request.user.userprofile.pk})



class RestaurantDeleteView(LoginRequiredMixin,DeleteView):
    model = UserProfile
    template_name = 'restaurants/restaurants-delete.html'
    success_url = f'/restaurants/list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            request.user.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Http404


def HeaderFilter(request):
    title_contains_query = request.GET.get('title_contains')











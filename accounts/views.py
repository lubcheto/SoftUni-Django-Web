from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm
from accounts.models import UserProfile
from restaurants.models import Restaurants


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'


    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get('choice_field')=="1":
            profile = Restaurants(user=user,)
            profile.is_restaurant=True
        else:
            profile = UserProfile(user=user, )
        user.save()
        profile.save()
        valid = super().form_valid(form)
        '''Authenticate the user and keep him logged in '''
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_success_url(self):
        if self.object.userprofile.is_restaurant:
            return reverse_lazy('restaurants details', kwargs={'pk': self.object.userprofile.id})
        else:
            return reverse_lazy('restaurants details', kwargs={'pk': self.object.userprofile.id})



class LoginViewCustom(LoginView):

    template_name = 'accounts/login.html'




@login_required
def logout_user(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))
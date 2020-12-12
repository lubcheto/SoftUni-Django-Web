from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, Http404

from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegisterForm, AccountEditForm
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
            return reverse_lazy('account details', kwargs={'pk': self.object.userprofile.id})



class LoginViewCustom(LoginView):
    template_name = 'accounts/login.html'




@login_required
def logout_user(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))


class AccountDetailsView(DetailView):
    model = UserProfile
    template_name = 'accounts/accounts-details.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = (self.request.user.id == self.object.user_id)
        context['can_delete'] = (self.request.user.id == self.object.user_id)

        return context

class AccountEditView(LoginRequiredMixin,UpdateView):
    model = UserProfile
    form_class = AccountEditForm
    template_name = 'accounts/account-edit.html'
    success_url = f'/restaurants/list/'

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.request.user.userprofile.pk})

class AccountDeleteView(LoginRequiredMixin,DeleteView):
    model = UserProfile
    template_name = 'accounts/accounts-delete.html'
    success_url = f'/restaurants/list/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            request.user.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Http404






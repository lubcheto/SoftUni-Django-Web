from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm
from accounts.models import UserProfile


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save(commit=False)
        profile = UserProfile(user=user, )
        user.save()
        profile.save()
        valid = super().form_valid(form)
        '''Authenticate the user and keep him logged in '''
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid




@login_required
def logout_user(request):
    logout(request)
    return redirect('%s?next=%s' % (settings.LOGOUT_URL, request.path))
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import RegistrationForm, AuthForm


def home(request):
    return render(
        request,
        'home.html'
    )


class Signup(FormView):
    template_name = 'registration/signup.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password2']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)


class MyLogin(FormView):
    template_name = 'registration/login.html'
    form_class = AuthForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return render(self.request, self.template_name, {'form': form, 'auth_error': True})

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'auth_error': True})


def my_logout(request):
    logout(request)
    return render(
        request,
        'gratitude.html',
    )

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from app_auth.forms import PrimaryUserCreationForm
from decorators import only_authenticated, only_not_authenticated


class RegisterView(View):
    @only_not_authenticated
    def get(self, request):
        form = PrimaryUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/register.html', context)

    @only_not_authenticated
    def post(self, request):
        form = PrimaryUserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('app_profile:profile')
        return render(request, 'app_auth/register.html', context)


class LoginView(View):
    @only_not_authenticated
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/login.html', context)

    @only_not_authenticated
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app_profile:profile')
        else:
            error_message = 'Невірне ім\'я користувача або пароль'
            context = {
                'error_message': error_message,
                'form': form,
            }
            return render(request, 'auth_app/login.html', context)


class LogoutView(View):
    @only_authenticated
    def get(self, request):
        logout(request)
        return redirect('app_main:index')

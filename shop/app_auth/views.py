from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from app_auth.forms import PrimaryUserCreationForm


class RegisterView(View):
    def get(self, request):
        form = PrimaryUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/register.html', context)

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
                return redirect('app_profile:profile')  # Перенаправлення на сторінку після успішного входу
        return render(request, 'app_auth/register.html', context)


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app_profile:profile')  # Перенаправлення на сторінку після успішного входу
            else:
                error_message = 'Невірне ім\'я користувача або пароль'
                return render(request, 'auth_app/login.html', {'error_message': error_message})

            # Виконати необхідні дії після успішного входу
            return redirect('app_main:index')  # Перенаправлення на сторінку після успішного входу

        return render(request, 'app_auth/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('app_main:index')

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'app_auth/register.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('auth_app/login')  # Перенаправлення на сторінку входу після успішної реєстрації
        return render(request, 'registration/register.html', context)


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
                return redirect('app_main:index')  # Перенаправлення на сторінку після успішного входу
            else:
                error_message = 'Невірне ім\'я користувача або пароль'
                return render(request, 'auth_app/login.html', {'error_message': error_message})
            print(username, password)
            # Виконати необхідні дії після успішного входу
            return redirect('app_main:index')  # Перенаправлення на сторінку після успішного входу

        return render(request, 'app_auth/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('app_main:index')

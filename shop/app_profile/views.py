from django.shortcuts import render
from django.views import View

from decorators import only_authenticated


class ProfileView(View):
    @only_authenticated
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_profile/profile.html', context=context)
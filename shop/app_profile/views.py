from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'app_profile/profile.html', context=context)
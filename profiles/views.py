from django.shortcuts import render, get_object_or_404
from .models import UserPage


def profile(request):
    profile = get_object_or_404(UserPage, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile':profile,
    }

    return render(request, template, context)
    
from django.shortcuts import render, get_object_or_404
from django.contrib import messages 
from .models import UserPage
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserPage, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Details have updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form':form,
        'orders':orders,
        
    }

    return render(request, template, context)
    
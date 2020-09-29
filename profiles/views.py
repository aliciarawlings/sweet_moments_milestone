from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserPage
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib.auth.models import User


def profile(request):
    print(request.user)
    user = get_object_or_404(User, username=request.user)
    profile = get_object_or_404(UserPage, user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Details have updated successfully')

    form = UserProfileForm(instance=profile)
    orders = user.orders.all()
    print(orders[0])

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)




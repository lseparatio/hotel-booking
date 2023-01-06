from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from settings.models import TopNav


@login_required
def profile(request):
    if 'ro' in request.LANGUAGE_CODE:
        topnav = TopNav.objects.language('ro').all()
    else:
        topnav = TopNav.objects.language('en').all()
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST, instance=profile)
        if form_profile.is_valid():
            form_profile.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form_profile = UserProfileForm(instance=profile)
    # orders = profile.orders.all()

    template = 'profiles/index.html'
    context = {
        'form_profile': form_profile,
        'profile': profile,
        'topnav': topnav,
        # s'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'profiles/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

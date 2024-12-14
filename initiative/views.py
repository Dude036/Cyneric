from django.contrib import auth
from django.shortcuts import render

# Create your views here.
def index(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'is_admin': user.is_authenticated,
    }
    return render(request, 'initiative_tracker.html', context)



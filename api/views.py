from django.shortcuts import render

# Usage Guide content
def api(request):
    return render(request, 'api.html', {})



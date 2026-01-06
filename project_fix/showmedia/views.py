from django.shortcuts import render

# Create your views here.

def photos_view(request):
    return render(request, 'show/photos.html')
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')



def about(request):
    context = {
        "name": "Mohapi home you are doing owk ",
        "Viper": "Tuwane Mohapi",
        "Code": 224
    }
    return render(request, 'main/about.html', context)
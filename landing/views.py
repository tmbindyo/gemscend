from django.shortcuts import render

# Create your views here.


# index dark
def index(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'index.html', context)


def faqs(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'faq.html', context)


def about_us(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'about_us.html', context)


def legal(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'legal.html', context)

def refer_and_earn(request):
    # Create a context dictionary with the user groups
    context = {
        'user': None
    }
    return render(request, 'refer_and_earn.html', context)


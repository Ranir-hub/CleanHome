from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def deliverypayment(request):
    return render(request, 'deliverypayment.html')
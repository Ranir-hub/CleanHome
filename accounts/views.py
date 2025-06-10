from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

from accounts.forms import SignUpForm, LoginForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_page = request.POST.get('next', '/')
            return redirect(next_page)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_page = request.POST.get('next', '/')
            return redirect(next_page)
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        next_page = request.POST.get('next', '/')
        return redirect(next_page)
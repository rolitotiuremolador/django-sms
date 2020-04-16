from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def signup(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(req, 'signup.html', {'form': form})


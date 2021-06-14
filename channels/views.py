from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import UserAccount


def become_user(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            user = UserAccount.objects.create(name=user.username, created_by=user)
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
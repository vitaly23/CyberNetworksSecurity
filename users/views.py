from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created Successfully, You are now able to log im')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')



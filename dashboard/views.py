from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])  # Specify the allowed HTTP methods
def dashboard(request):
    # Add dashboard logic here
    return render(request, 'dashboard/dashboard.html')


@require_http_methods(["POST"])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})


@require_http_methods(["POST"])
def user_logout(request):
    logout(request)
    return redirect('user_login')

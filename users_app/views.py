from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        reg_form = CustomRegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, ("New User Account Created"))
            return redirect('login')
    else:
        reg_form = CustomRegisterForm()
    return render(request, 'register.html', {'reg_form':reg_form})

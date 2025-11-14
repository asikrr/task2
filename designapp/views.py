from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from .forms import SignupForm
from django.contrib.auth import login

from .models import DesignRequest

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    return render(request, 'registration/profile.html')

class DesignRequestCreate(LoginRequiredMixin, generic.CreateView):
    model = DesignRequest
    fields = ['title', 'description', 'category', 'image']

class DesignRequestList(LoginRequiredMixin, generic.ListView):
    model = DesignRequest

class DesignRequestDetail(LoginRequiredMixin, generic.DetailView):
    model = DesignRequest
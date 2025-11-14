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

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.customer = self.request.user
        fields.save()
        return super().form_valid(form)


class DesignRequestDetail(LoginRequiredMixin, generic.DetailView):
    model = DesignRequest


class DesignRequestUserList(LoginRequiredMixin, generic.ListView):
    model = DesignRequest
    template_name = 'designapp/designrequest_user_list.html'
    context_object_name = 'designrequest_user_list'

    def get_queryset(self):
        queryset = DesignRequest.objects.filter(customer=self.request.user)
        return queryset


class DesignRequestAllList(LoginRequiredMixin, generic.ListView):
    model = DesignRequest
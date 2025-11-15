from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import SignupForm, DesignRequestUpdateForm
from django.contrib.auth import login
from django.contrib import messages

from .models import DesignRequest, Category


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


class CategoryList(generic.ListView):
    model = Category


class CategoryCreate(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = ['title']


class CategoryDelete(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = '/'


class DesignRequestCreate(LoginRequiredMixin, generic.CreateView):
    model = DesignRequest
    fields = ['title', 'description', 'category', 'image']

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.customer = self.request.user
        fields.save()
        return super().form_valid(form)


class DesignRequestDelete(LoginRequiredMixin, generic.DeleteView):
    model = DesignRequest
    success_url = '/'


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
    template_name = 'designapp/designrequest_all_list.html'
    context_object_name = 'designrequest_all_list'


@login_required
def designrequest_update(request, pk):
    designrequest = get_object_or_404(DesignRequest, pk=pk)

    if request.method == 'POST':
        form = DesignRequestUpdateForm(request.POST, request.FILES, instance=designrequest)
        if form.is_valid():
            form.save()
            return redirect('designrequest-detail', pk=designrequest.pk)
    else:
        form = DesignRequestUpdateForm(instance=designrequest)

    return render(request, 'designapp/designrequest_update_form.html', {'form': form, 'designrequest': designrequest})
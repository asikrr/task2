from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .filters import DesignRequestFilter
from .forms import SignupForm, DesignRequestForm, DesignRequestUpdateForm
from django.contrib.auth import login

from .models import DesignRequest, Category


def index(request):
    num_designrequests_in_work = DesignRequest.objects.filter(status='w').count()
    latest_done_designrequests_list = DesignRequest.objects.filter(status='d')[:4]

    return render(request, 'index.html', {'num_designrequests_in_work': num_designrequests_in_work,
                                          'latest_done_designrequests_list': latest_done_designrequests_list})


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()

    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'registration/profile.html')


class DesignRequestUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = DesignRequest
    form_class = DesignRequestUpdateForm
    template_name = 'designapp/designrequest_update_form.html'
    context_object_name = 'designrequest'
    permission_required = 'can_change_designrequest'
    success_url = reverse_lazy('designrequest-all-list')


class CategoryList(PermissionRequiredMixin, generic.ListView):
    model = Category
    permission_required = 'can_view_category'


class CategoryCreate(PermissionRequiredMixin, generic.CreateView):
    model = Category
    fields = ['title']
    permission_required = 'can_add_category'


class CategoryDelete(PermissionRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    permission_required = 'can_delete_category'


class DesignRequestCreate(LoginRequiredMixin, generic.CreateView):
    model = DesignRequest
    form_class = DesignRequestForm

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.customer = self.request.user
        fields.save()
        return super().form_valid(form)


class DesignRequestDelete(LoginRequiredMixin, generic.DeleteView):
    model = DesignRequest
    success_url = reverse_lazy('designrequest-user-list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status != 'n':
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class DesignRequestDetail(LoginRequiredMixin, generic.DetailView):
    model = DesignRequest


class DesignRequestUserList(LoginRequiredMixin, generic.ListView):
    model = DesignRequest
    template_name = 'designapp/designrequest_user_list.html'
    context_object_name = 'designrequest_user_list'

    def get_queryset(self):
        queryset = DesignRequest.objects.filter(customer=self.request.user)
        self.filterset = DesignRequestFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class DesignRequestAllList(PermissionRequiredMixin, generic.ListView):
    model = DesignRequest
    template_name = 'designapp/designrequest_all_list.html'
    context_object_name = 'designrequest_all_list'
    permission_required = 'can_change_status'

    def get_queryset(self):
        queryset = DesignRequest.objects.all()
        self.filterset = DesignRequestFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context
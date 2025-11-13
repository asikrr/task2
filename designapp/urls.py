from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('designrequest/create/', views.DesignRequestCreate.as_view(), name='designrequest-create'),
]
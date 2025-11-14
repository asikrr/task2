from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('designrequest/create/', views.DesignRequestCreate.as_view(), name='designrequest-create'),
    path('designrequests/', views.DesignRequestList.as_view(), name='designrequest-list'),
    path('designrequest/<int:pk>/', views.DesignRequestDetail.as_view(), name='designrequest-detail'),
]
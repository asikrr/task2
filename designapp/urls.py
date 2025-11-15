from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('designrequest/create/', views.DesignRequestCreate.as_view(), name='designrequest-create'),
    path('designrequestsall/', views.DesignRequestAllList.as_view(), name='designrequest-all-list'),
    path('designrequest/<int:pk>/', views.DesignRequestDetail.as_view(), name='designrequest-detail'),
    path('designrequestsuser/', views.DesignRequestUserList.as_view(), name='designrequest-user-list'),
    path('designrequest/delete/<int:pk>/', views.DesignRequestDelete.as_view(), name='designrequest-delete'),
]
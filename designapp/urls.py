from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('designrequestsall/', views.DesignRequestAllList.as_view(), name='designrequest-all-list'),
    path('designrequestsuser/', views.DesignRequestUserList.as_view(), name='designrequest-user-list'),
    path('designrequest/<int:pk>/', views.DesignRequestDetail.as_view(), name='designrequest-detail'),
    path('designrequest/create/', views.DesignRequestCreate.as_view(), name='designrequest-create'),
    path('designrequest/delete/<int:pk>/', views.DesignRequestDelete.as_view(), name='designrequest-delete'),
    path('categorys/', views.CategoryList.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('category/delete/<int:pk>/', views.CategoryDelete.as_view(), name='category-delete'),
    path('designrequest/update/<int:pk>/', views.DesignRequestUpdate.as_view(), name='designrequest-update'),
]

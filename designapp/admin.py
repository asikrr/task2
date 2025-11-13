from django.contrib import admin
from .models import Category, DesignRequest, CustomUser

admin.site.register(CustomUser)

class DesignRequestsInstanceInline(admin.TabularInline):
    model = DesignRequest
    extra = 0

@admin.register(DesignRequest)
class DesignRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    list_filter = ('status', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (DesignRequestsInstanceInline,)
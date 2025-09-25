from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'price', 'certification', 'is_active', 'created_at']
    list_filter = ['is_active', 'certification', 'created_at']
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['is_active', 'price']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Course Details', {
            'fields': ('duration', 'price', 'features')
        }),
        ('Settings', {
            'fields': ('certification', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

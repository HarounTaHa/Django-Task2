from django.contrib import admin
from .models import Course, Instructor


class InstructorAdmin(admin.ModelAdmin):
    readonly_fields = ['share_percentage']
    list_display = ['name', 'country', 'payment', 'salary', 'share_percentage']


# Register your models here.
admin.site.register(Course)
admin.site.register(Instructor, InstructorAdmin)

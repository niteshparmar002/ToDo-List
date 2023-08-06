from django.contrib import admin
from home.models import Task

# Register your models here.
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription')
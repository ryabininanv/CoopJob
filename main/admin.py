from django.contrib import admin

from main.models import Task


class TaskAdmin(admin.ModelAdmin):
    title = ['title', 'type', 'user','deadlinedate', "deadlinetime",'file_task','status']
    search_fields = ['title', 'user', 'type']
    list_filter = ['user']
    list_display = ['title', 'type', 'user','deadlinedate','file_task','status']
    editable_list = ['title', 'type']


admin.site.register(Task, TaskAdmin)
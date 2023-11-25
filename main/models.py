from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django.contrib.admin import widgets


class Task(models.Model):
    status_list = (("100", "Открыт",), ("101", "В работе"), ("102", "Закрыт"))
    deadlinedate = models.DateField(blank=True, null=True)
    deadlinetime = models.TimeField(blank=True, null=True)
    file_task = models.FileField(blank=True, null=True)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=status_list, default=100)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET(None))
    created_on = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.title

    def set_manger(self, user):
        self.user = user

    def get_deadline(self):
        return self.deadlinedate.strftime("%d.%m.%Y ")+self.deadlinetime.strftime("%H:%M")

    def get_created(self):
        return self.created_on.strftime("%d.%m.%Y %H:%M")

    def check_deadline(self):
        return datetime.now().date() >= self.deadlinedate and datetime.now().time() > self.deadlinetime


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'type', 'file_task', "deadlinedate", "deadlinetime"]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields["deadlinedate"].widget = widgets.AdminDateWidget()
        self.fields["deadlinetime"].widget = widgets.AdminTimeWidget()
        print()

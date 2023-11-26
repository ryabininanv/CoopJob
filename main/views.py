from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from main import forms
from main.models import Task, TaskForm


def home(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        task = Task.objects.filter(id=request.POST["task"]).first()
        task.set_manger(request.user)
        task.status = "101"
        task.save()
    task = Task.objects.all()
    context = {'tasks': task, "ismanager": request.user.has_perm("main.add_task"), 'user': request.user,
               "is_auth": request.user.is_authenticated}
    return render(request, 'main.html', context)


def loginPage(request):
    return render(request, 'login.html')


def doLogout(request):
    logout(request)
    return redirect('home')


# страница входа
def loginPage(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'login.html', {'form': form})


def mytask(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        task = Task.objects.filter(id=request.POST["task"]).first()
        task.set_manger(request.user)
        task.status = "102"
        task.save()
    task = Task.objects.filter(user=request.user)
    context = {'tasks': task, "ismanager": request.user.has_perm("main.add_task"), 'user': request.user,
               "is_auth": request.user.is_authenticated}
    return render(request, 'mytask.html', context)


def about(request):
    context = {"ismanager": request.user.has_perm("main.add_task"), 'user': request.user,
               "is_auth": request.user.is_authenticated}
    return render(request, 'about.html', context)


def addtask(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect("home")
            except Exception as Ex:
                print(Ex)
                form.add_error(None, 'Ошибка добавления задачи')
    form = TaskForm()
    context = {"ismanager": request.user.has_perm("main.add_task"), 'user': request.user, "form": form,
               "is_auth": request.user.is_authenticated}
    return render(request, 'addtask.html', context)

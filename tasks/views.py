from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task
from .forms import TaskForm

# Create your views here.


def home(req):
    return render(req, "home.html")


def auth_signup(req):
    if req.method == "GET":
        return render(req, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if req.POST["password1"] == req.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=req.POST["username"], password=req.POST["password1"]
                )
                user.save()
                login(req, user)
                return redirect("tasks")
            except IntegrityError:
                return render(req, "signup.html", {
                    "form": UserCreationForm,
                    "error": "Username already in use"
                })
        else:
            return render(req, "signup.html", {
                "form": UserCreationForm,
                "error": "Passwords do not match"
            })


def auth_signin(req):
    if req.method == "GET":
        return render(req, "signin.html", {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            req, username=req.POST["username"], password=req.POST["password"])
        if user is None:
            return render(req, "signin.html", {
                "form": AuthenticationForm,
                "error": "Invalid credentials"
            })
        else:
            login(req, user)
            return redirect("tasks")


@login_required
def auth_signout(req):
    logout(req)
    return redirect('home')


@login_required
def tasks(req):
    all_tasks = Task.objects.filter(user=req.user)
    pending_tasks = Task.objects.filter(
        user=req.user, completed_at__isnull=True)
    completed_tasks = Task.objects.filter(
        user=req.user, completed_at__isnull=False)
    return render(req, "tasks.html", {
        "tasks": all_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks
    })


@login_required
def create_task(req):
    if req.method == "GET":
        return render(req, "create_task.html", {
            "form": TaskForm
        })
    else:
        try:
            form = TaskForm(req.POST)
            new_task = form.save(commit=False)
            new_task.user = req.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(req, "create_task.html", {
                "form": TaskForm,
                "error": "Error creating task"
            })


@login_required
def task_detail(req, task_id):
    if req.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=req.user)
        form = TaskForm(instance=task)
        return render(req, "task_detail.html", {
            "task": task,
            "form": form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id)
            form = TaskForm(req.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(req, "task_detail.html", {
                "task": task,
                "form": TaskForm,
                "error": "Error updating task"
            })


@login_required
def complete_task(req, task_id):
    task = get_object_or_404(Task, pk=task_id, user=req.user)
    if req.method == "POST":
        task.completed_at = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(req, task_id):
    task = get_object_or_404(Task, pk=task_id, user=req.user)
    if req.method == "POST":
        task.delete()
        return redirect('tasks')

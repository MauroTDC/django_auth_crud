from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.auth_signup, name="signup"),
    path("signin/", views.auth_signin, name="signin"),
    path("signout/", views.auth_signout, name="signout"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/create/", views.create_task, name="create_task"),
    path("tasks/<int:task_id>", views.task_detail, name="task_detail"),
    path("tasks/<int:task_id>/completed",
         views.complete_task, name="complete_task"),
    path("tasks/<int:task_id>/delete", views.delete_task, name="delete_task")
]

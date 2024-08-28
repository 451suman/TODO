from django.urls import path
from todo_app import views


urlpatterns = [
    path('', views.todo_list, name="list"),
    path("delete/<int:id>/" ,views.todo_delete, name="delete"),
    # path("update/<int:id>/" ,views.todo_update, name="update"),
    path("modify/<int:id>/" ,views.todo_update, name="update"),
    path("create/",views.todo_create, name="create"),
]
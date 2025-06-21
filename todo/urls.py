from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # list 목록보기 

    # 탬플릿Views
    path("list/", views.TodoListViews.as_view(), name="todo_List"), # list 목록보기
    path("create/", views.TodoCreateViews.as_view() , name="todo_Create"),
    path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),


    # apiViews
    path("api/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
    path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),
    path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),

]

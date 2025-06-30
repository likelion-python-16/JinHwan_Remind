from django.urls import path, include
from . import views
# from . import api_views  api_views.py
# from .api_views import (
#     TodoGenericsListAPI, 
#     TodoGenericsCreateAPI, 
#     TodoGenericsRetrieveAPI, 
#     TodoGenericsUpdateAPI,
#     TodoGenericsDeleteAPI,
#     TodoGenericsListCreateAPI,
#     TodoGenericsRetrieveUpdateDeleteAPI,
# )

from . api_views import (
    TodoListAPI,
    TodoCreateAPI,
    TodoRetrieveAPI,
    TodoUpdateAPI,
    TodoDeleteAPI,
    TodoGenericsListAPI, 
    TodoGenericsCreateAPI, 
    TodoGenericsRetrieveAPI, 
    TodoGenericsUpdateAPI,
    TodoGenericsDeleteAPI,
    TodoGenericsListCreateAPI,
    TodoGenericsRetrieveUpdateDeleteAPI, 
    TodoViewSet,
    CustomLogoutAPI,

)

from rest_framework.routers import DefaultRouter

app_name ="todo"

router = DefaultRouter()
router.register(r"view", TodoViewSet, basename="todo") 

urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # list 목록보기 

    # 탬플릿Views
    path("list/", views.TodoListViews.as_view(), name="todo_List"), # list 목록보기
    path("create/", views.TodoCreateViews.as_view() , name="todo_Create"),
    path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", views.TodoUpdateViews.as_view(), name="todo_Update"),

    # apiViews
    path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
    path("api/create/", TodoCreateAPI.as_view(), name="todo_api_create"),
    path("api/retrieve/<int:pk>/", TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("api/update/<int:pk>/", TodoUpdateAPI.as_view(), name="todo_api_update"),
    path("api/delete/<int:pk>/", TodoDeleteAPI.as_view(), name="todo_api_delete"),

    #GenericAPIView
    path("generics/list/", TodoGenericsListAPI.as_view(), name="todo_api_list"),
    path("generics/create/", TodoGenericsCreateAPI.as_view(), name="todo_api_create"),
    path("generics/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("generics/update/<int:pk>/",TodoGenericsUpdateAPI.as_view(), name="todo_api_update"),
    path("generics/delete/<int:pk>/",TodoGenericsDeleteAPI.as_view(), name="todo_api_delete"),

    #GenericAPIView + Mixin
    path("generics/", TodoGenericsListCreateAPI.as_view(), name="todo_generics_list_create"),
    path("generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_generics_detail"),

    # ViewSets
    path("viewsets/", include(router.urls)), # /todo/viewsets/view/

    # logout API
    path("api/custom-logout/", CustomLogoutAPI.as_view(), name="custom-logout"),

]

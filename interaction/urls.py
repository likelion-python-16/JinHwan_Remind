from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import LikeViewSet, BookmarkViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")
router.register(r"bookmarks", BookmarkViewSet, basename="bookmarks")
router.register(r"comments", CommentViewSet, basename="comments")
# r은 주소의 마지막을 표시한 것이며 규칙이 아닌 관습이다.

app_name = "interaction"

urlpatterns = [
    path("", include(router.urls)),
]

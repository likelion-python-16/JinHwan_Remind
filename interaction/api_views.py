
from rest_framework import viewsets
from .models import Like, Bookmark, Comment, CommentLike
from .serializers import LikeSerializer, BookmarkSerializer, CommentSerializer 
from rest_framework import permissions
from rest_framework.decorators import action
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.response import Response
from .serializers import CommentLikeSerializer
from django.shortcuts import get_object_or_404


class LikeViewSet(viewsets.ModelViewSet): # 좋아요 기능을 위한 ViewSet
    queryset = Like.objects.all() # 모든 Like 객체를 기본 조회 대상으로 사용
    serializer_class = LikeSerializer # LikeSerializer를 사용해 직렬화/역직렬화 처리
    permission_classes = [permissions.IsAuthenticated] # 로그인한 사용자만 요청 가능

    @action(detail=True, methods=["post"]) # /likes/{pk}/toggle/ 형태로 POST 요청 허용
    def toggle(self, request, pk=None): # 좋아요 토글 기능 (누르면 추가, 다시 누르면 취소)
        todo = Todo.objects.get(pk=pk) # 대상 Todo 객체 가져오기
        user = request.user # 현재 요청한 유저

        like, created = Like.objects.get_or_create(todo=todo, user=user) # 이미 있으면 가져오고, 없으면 생성
        like.is_like = not like.is_like # 현재 상태 반전 (True → False or False → True)
        like.save() # 변경 사항 저장

        serializer = TodoSerializer(todo, context={"request": request}) # Todo 객체를 직렬화해서 응답에 포함
        return Response(serializer.data) # 변경된 Todo 정보 반환


class BookmarkViewSet(viewsets.ModelViewSet): # 북마크 기능을 위한 ViewSet
    queryset = Bookmark.objects.all() 
    serializer_class = BookmarkSerializer 
    permission_classes = [permissions.IsAuthenticated] 

    @action(detail=True, methods=["post"]) 
    def toggle(self, request, pk=None): 
        todo = Todo.objects.get(pk=pk) 
        user = request.user

        bookmark, created = Bookmark.objects.get_or_create(todo=todo, user=user) 
        bookmark.is_marked = not bookmark.is_marked 
        bookmark.save() 

        serializer = TodoSerializer(todo, context={"request": request}) 
        return Response(serializer.data) 

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        todo_id = self.request.query_params.get("todo_pk")
        return Comment.objects.filter(todo_id=todo_id).order_by("-created_at")

    def perform_create(self, serializer):
        todo_id = self.request.data.get("todo_pk")
        todo = Todo.objects.get(pk=todo_id)
        serializer.save(user=self.request.user, todo=todo)

class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])  # /commentlikes/{pk}/toggle/
    def toggle(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user
        like, created = CommentLike.objects.get_or_create(comment=comment, user=user)
        like.is_like = not like.is_like
        like.save()
        return Response({
            "is_liked": like.is_like,
            "like_count": CommentLike.objects.filter(comment=comment, is_like=True).count()
        })
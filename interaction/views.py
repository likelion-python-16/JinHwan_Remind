from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from interaction.models import Like, Bookmark, Comment

# 로그인하지 않은 사용자가 이 뷰를 실행하지 못하도록 막아주는 데이코레이션
@login_required # 로그인확인여부에 따라 접근금지 또는 로그인 페이지 보내기 역할
def todo_detail_with_interaction(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user

    like_obj = Like.objects.filter(todo=todo, is_like=True).first()

    like_count = Like.objects.filter(todo=todo, is_like=True).count()

    bookmark_obj = Bookmark.objects.filter(todo=todo, user=user).first()
    
    comments = Comment.objects.filter(todo=todo).order_by("-created_at")
    
    context = {
        "todo": todo,
        "like_obj" : like_obj,
        "like_count": like_count,
        "bookmark_obj": bookmark_obj,
        "comments": comments,
    } # 예시 {interaction:like_obj}
    return render(request, "interaction/todo_detail.html", context)
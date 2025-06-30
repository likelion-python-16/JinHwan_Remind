from django.db import models
from todo.models import Todo
from django.contrib.auth.models import User

# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE) 
    
    is_like = models.BooleanField(default=True)

    class Meta: # 중복 방지
        unique_together = ("user", "todo")
        # todo, user속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"   
        # admin ❤️ 공부하기 

# 북마크 모델
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE) 
    is_marked = models.BooleanField(default=True)

    class Meta: # 중복 방지
        unique_together = ("user", "todo")
        # todo, user속성은 중복 데이터를 아예 저장하지 못하게 막아주는 제약조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"   
        # admin ❤️ 공부하기 

# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 댓글을 좋아요를 누른 유저들을 저장하는 필드
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)

    def __str__(self):
        return f"{self.user.username} ❤️ {self.content[:20]}"   
        # admin ❤️ 공부하기 
from .models import Like, Bookmark, Comment
from rest_framework import serializers


# user.username, todo.name

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    # 이필드는 확인용으로 읽기전용 

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields = ["user"]

# read_only=True: 이 필드는 출력전용으로 클라언트가 값을 보내도 저장에는 사용되지 않습니다. 

class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields = ["user"]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True) 

    todo_name = serializers.CharField(source="todo.name", read_only=True)

    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "todo", "todo_name", "user", "username", "content", "created_at", "like_count", ]
        read_only_fields = ["todo","user","created_at"] 
        # 폼에서 사용자가 수정할수 없어야 하는 필드를 명확히 구분해주기 위한 용도

    def get_like_count(self, obj):
        return obj.likes.count() 
    
    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

# 시리얼라이저의 역할
# 유효성 검증, 프리젠테이션 로직을 처리한다.
# 화면에 표시되는 방식, 스타일과 관련된 로직을 처리한다.
# 그 값을 어떻게 보여줄것이냐? 


from .models import CommentLike
# M2M 추가

class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True) 

    comment_content = serializers.CharField(source="comment.content", read_only=True)

    class Meta:
        model = CommentLike
        fields = ["id", "user", "username", "comment", "comment_content", "is_like"]
        read_only_fields = ["user"]
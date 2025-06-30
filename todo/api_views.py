from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser


# 전체보기
class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)  # 일반 json데이터 .data


# 생성하기
class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


# 상세조회
class TodoRetrieveAPI(APIView):  # 개발자가 커스터마이징 형식으로 짜놓은 API 상세조회
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo)
        return Response(serializer.data)


# 수정하기
class TodoUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data)
        # serializer.is_valid(raise_exception=True)

        if not serializer.is_valid():
            print("PATCH 유효성 오류:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


# 삭제하기
class TodoDeleteAPI(APIView):
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# DRF_GenericAPIView
# list
class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# create
class TodoGenericsCreateAPI(generics.CreateAPIView):
    serializer_class = TodoSerializer


# retrieve(상세조회)
class TodoGenericsRetrieveAPI(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# update(수정)
class TodoGenericsUpdateAPI(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# destroy
class TodoGenericsDeleteAPI(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# ListCreate
class TodoGenericsListCreateAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# retrieveUpdateDelete
class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

from .pagination import CustomPageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


# DRF_ViewSets
# viewSet
class TodoViewSet(viewsets.ModelViewSet):
    # queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer

    # pagination
    pagination_class = CustomPageNumberPagination

    # 인증 
    authenticateion_classes = [SessionAuthentication]

    # 권한
    permission_classes = [IsAuthenticated]

    # 이미지
    parser_classes = [MultiPartParser, FormParser]

    # 검색기능 
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]



    def get_queryset(self):  
        qs = Todo.objects.all().order_by("-created_at")
        print("정렬된 queryset preview:", list(qs[:3]))  # 서버 로그 확인용
        return qs

from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomLogoutAPI(APIView):
    def get(self, request): # 상태 변화가 일어나는 요청
        logout(request)
        return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
        # return redirect('todo_List')

    # def post(self, request):
        # logout(request)
        # return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
        # return redirect('todo_List')



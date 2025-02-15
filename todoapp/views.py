from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import todoSerializer

class TodoAPIView(APIView):
    def get(self,request):
        todos = Todo.objects.all()
        serializer = todoSerializer(todos,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = todoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
class TodoDetailAPIView(APIView):
    def get(self,request,pk):
        todo = get_object_or_404(Todo,pk = pk)
        serializer = todoSerializer(todo)
        return Response(serializer.data)
    def post(self,request,pk):
        todo = get_object_or_404(Todo,pk=pk)
        serializer = todoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        todo = get_object_or_404(Todo,pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




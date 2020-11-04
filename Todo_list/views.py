from .serializers import TodoSerializer
from rest_framework import viewsets, permissions
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = TodoSerializer


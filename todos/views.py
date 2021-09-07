from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

cheese=5

class TodoViewSet(viewsets.ModelViewSet):
    ## Give it the main query for the index route
    queryset = Todo.objects.all()
    # THe serializer for serializing
    serializer_class = TodoSerializer
    ## Optional Permissions
    permission_classes = [permissions.AllowAny]
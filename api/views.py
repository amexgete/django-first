from rest_framework import generics 

from .serializers import TaskSerializer

from .models import Task

class tasklist(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class taskdel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer	
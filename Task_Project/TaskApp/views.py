from rest_framework import generics, filters, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from django.contrib.auth.models import User

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# List view for all tasks
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] 
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'status', 'priority']  # Allow searching by title, status, and priority
    ordering_fields = ['due_date', 'priority', 'created_at']

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)  # Assign the task to the currently logged-in user

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Detail view for a specific task by ID
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return super().get_object()
        except Task.DoesNotExist:
            raise NotFound(detail="Task not found.")

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Task.DoesNotExist:
            raise NotFound(detail="Task not found.")
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

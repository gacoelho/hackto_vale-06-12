from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Team, Employee, Task
from .serializers import CustomUserSerializer, TeamSerializer, EmployeeSerializer, TaskSerializer

# ViewSet para CustomUser
class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# ViewSet para Team
class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# ViewSet para Employee
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['post'])
    def recruit(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'])
    def fire(self, request, pk=None):
        try:
            employee = self.get_object()
            employee.delete()
            return Response({"detail": "Funcionário demitido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Employee.DoesNotExist:
            return Response({"detail": "Funcionário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['post'])
    def assign_task(self, request, pk=None):
        try:
            employee = self.get_object()
            task_id = request.data.get("task_id")
            task = Task.objects.get(id=task_id)
            task.assigned_to = employee
            task.save()
            return Response({"detail": f"Tarefa '{task.title}' atribuída ao funcionário '{employee.first_name}'."}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def assign_team(self, request, pk=None):
        try:
            employee = self.get_object()
            team_id = request.data.get("team_id")
            team = Team.objects.get(id=team_id)
            employee.team = team
            employee.save()
            return Response({"detail": f"Funcionário '{employee.first_name}' foi atribuído ao time '{team.name}'."}, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"detail": "Time não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# ViewSet para Task
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


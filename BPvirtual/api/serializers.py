from rest_framework import serializers
from .models import CustomUser, Team, Employee, Task

# CustomUser Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile_picture', 'is_staff', 'is_active']

# Team Serializer
class TeamSerializer(serializers.ModelSerializer):
    leader = CustomUserSerializer(read_only=True)  # Inclui detalhes do líder na resposta
    employee_count = serializers.IntegerField(read_only=True)  # Campo personalizado do modelo

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'leader', 'employee_count']

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)
    tasks = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), many=True, required=False)

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'position', 'team', 'date_joined', 'tasks']

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), allow_null=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'team', 'due_date', 'completed']

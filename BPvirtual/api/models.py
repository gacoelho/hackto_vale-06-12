from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Sobrescrevendo os campos com related_name únicos
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Nome único para o reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Nome único para o reverse accessor
        blank=True
    )

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    leader = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='teams',
        help_text="User is the leader of this team;"
    )

    def __str__(self):
        return self.name
    
    def employee_count(self):
        return self.employee.count()

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100, blank=True, null=True, help_text="Cargo ou posição na empresa.")
    team=models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees",
        help_text="team of the associated with the employed."
    )
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position or 'Sem cargo'}"



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField(
        Employee, blank=True, related_name='tasks',
        help_text="Employee of the task."
    )
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks',
        help_text="Equipe relacionada a esta tarefa."
    )
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {'Concluída' if self.completed else 'Pendente'}"

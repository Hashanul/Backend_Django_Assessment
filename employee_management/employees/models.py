from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    achievements = models.ManyToManyField(Achievement, through='AchievementEmployee')
    
    def __str__(self):
        return self.name

class AchievementEmployee(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    achievement_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('achievement', 'employee')
    
    def __str__(self):
        return f"{self.employee.name} - {self.achievement.name}"
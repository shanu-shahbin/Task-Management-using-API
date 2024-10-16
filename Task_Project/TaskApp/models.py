from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        # Ensure due date is not in the past
        if self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")

        # Ensure logical status transition
        if self.status == 'completed' and self.pk:
            previous_status = Task.objects.get(pk=self.pk).status
            if previous_status not in ['in-progress']:
                raise ValidationError("Task must be 'in-progress' before being marked as 'completed'.")

    def save(self, *args, **kwargs):
        self.clean() 
        super(Task, self).save(*args, **kwargs)

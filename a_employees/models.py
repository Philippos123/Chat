from django.db import models
from django.contrib.auth.models import User

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_user_submissions')  # Different related_name
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission from {self.user.username} at {self.created_at}"

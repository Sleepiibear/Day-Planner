from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):

    title = models.CharField(max_length=254)
    description = models.TextField()
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

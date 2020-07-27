from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Letter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title





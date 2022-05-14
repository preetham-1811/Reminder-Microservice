from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    public = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['author', ]), ]
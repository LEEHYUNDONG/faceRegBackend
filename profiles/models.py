from django.db import models

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=10, blank=True, default='')
    name = models.TextField()

    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.studentId

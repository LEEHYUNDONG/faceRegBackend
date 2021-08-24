from django.db import models



class checkImage(models.Model):
    title = models.CharField(max_length=200, default='None')
    image = models.ImageField(upload_to='check', default='../media/james.jpg') 
    
    def __str__(self):
        return self.title

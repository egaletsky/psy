from django.db import models

class articlesForCouple(models.Model):
    number = models.IntegerField()    
    title = models.CharField(max_length = 20)
    text = models.TextField()
    
    def __str__(self):
        return self.title
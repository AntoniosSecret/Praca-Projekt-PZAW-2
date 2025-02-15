from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to="stylr/images")
    desc = models.TextField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    datetimePosted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nr {self.pk}: {self.desc[:10]} ({self.datetimePosted:%d-%m-%Y %H:%M})"
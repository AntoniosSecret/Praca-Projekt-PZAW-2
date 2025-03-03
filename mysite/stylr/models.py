from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="stylr/media/stylr/images")
    desc = models.TextField(max_length=200)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    datetimePosted = models.DateTimeField(auto_now_add=True)
    
    def num_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"Nr {self.pk} by {self.user}: {self.desc[:10]} ({self.datetimePosted:%d-%m-%Y %H:%M})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
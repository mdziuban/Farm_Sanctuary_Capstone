from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    suspended = models.BooleanField()

    def __str__(self):
        return self.display_name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='post_user')
    created = models.DateTimeField(auto_now_add=True)
    text_content = models.CharField(max_length=200, blank=True)
    img_content = models.ImageField(blank=True)
    hashtags = models.CharField(max_length=200, blank=True)

class Reply(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reply_user')
    reply_created = models.DateTimeField(auto_now_add=True)
    text_content = models.CharField(max_length=200, blank=True)
    img_content = models.ImageField(blank=True)

class GameData(models.Model):
    save_file = models.JSONField()
    user_id = models.ForeignKey(Player, models.PROTECT, related_name='gamedata')

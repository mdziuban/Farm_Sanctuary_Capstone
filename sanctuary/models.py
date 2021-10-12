from django.db import models


class Player(models.Model):
    display_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    bio = models.CharField(max_length=500)
    suspended = models.BooleanField()

    def __str__(self):
        return self.display_name

class Post(models.Model):
    user = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='user')
    created = models.DateTimeField(auto_now_add=True)
    text_content = models.CharField(max_length=200, blank=True)
    img_content = models.ImageField(blank=True)
    hashtags = models.CharField(max_length=200, blank=True)

class Reply(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='post')
    reply_created = models.DateTimeField(auto_now_add=True)
    text_content = models.CharField(max_length=200)
    img_content = models.ImageField()

class GameData(models.Model):
    save_file = models.JSONField()
    user_id = models.ForeignKey(Player, models.PROTECT, related_name='gamedata')

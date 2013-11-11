from django.db import models

class FollowedUser(models.Model):
    twitter_screen_name = models.CharField(max_length=40, unique=True, blank=False)
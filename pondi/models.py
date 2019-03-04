from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    first_name = models.CharField(max_length=50, null = True, blank = True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, default="olive")
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    closefriends = models.ManyToManyField("self", related_name='close' ,symmetrical = False)
    friends = models.ManyToManyField("self", symmetrical = True)
    pendingfriends = models.ManyToManyField("self", symmetrical=False)
    color = models.CharField(max_length = 50, default = "olive")
    animal = models.CharField(max_length=50, default="porcupine")



    def __str__(self):
        return self.user.username




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Prompt(models.Model):
    question = models.CharField(max_length = 250)

    def __str__(self):
        return self.question

class Post(models.Model):
    prompt = models.ForeignKey(Prompt, on_delete = models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    privacy = models.CharField(max_length = 1)
    theme = models.CharField(max_length = 500)

    def __str__(self):
        return self.profile.user.username + ' - ' + self.body

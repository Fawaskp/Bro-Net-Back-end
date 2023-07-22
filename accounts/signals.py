from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models.models2 import Follow
from .models.models import UserProfile,User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Follow)
def update_follow_counts(sender, instance, created, **kwargs):
    if created:

        followed_user = instance.followed_user
        following_user = instance.following_user

        followed_user_profile = UserProfile.objects.get(user=followed_user)
        followed_user_profile.followers_count += 1 
        followed_user_profile.save()

        following_user_profile = UserProfile.objects.get(user=following_user)
        following_user_profile.following_count += 1
        following_user_profile.save()

@receiver(post_delete, sender=Follow)
def update_follow_counts_on_delete(sender, instance, **kwargs):
    followed_user = instance.followed_user
    following_user = instance.following_user

    followed_user_profile = UserProfile.objects.get(user=followed_user)
    followed_user_profile.followers_count -= 1
    followed_user_profile.save()

    following_user_profile = UserProfile.objects.get(user=following_user)
    following_user_profile.following_count -= 1
    following_user_profile.save()
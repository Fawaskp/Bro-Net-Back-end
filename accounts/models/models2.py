from django.db import models

class SocialMedia(models.Model):
    icon = models.ImageField(upload_to='social-media-icons',null=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = ("Socila Media")

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    name  = models.CharField(max_length=30)
    icon  = models.ImageField('skill-icons')
    color = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    user            = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    name            = models.CharField(max_length=50)
    description     = models.TextField()
    logo            = models.ImageField('project-logo',null=True)
    repository_link = models.CharField(max_length=80)
    live_link       = models.CharField(max_length=30)
    skills_used     = models.ManyToManyField(Skill)

    class Meta:
        verbose_name_plural = ("Projects")

    def __str__(self):
        return f"{self.name} by {self.user.fullname}"

class Follow(models.Model):
    following_user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name='following_user_set')
    followed_user  = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name='followed_user_set')

    def __str__(self) -> str:
        return f"{self.following_user} followed {self.followed_user}"
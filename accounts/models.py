from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self,email, password=None , **extra_fields):
    
        if email is None:
            raise TypeError('Email Field Must Be Required')
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email = email,
            **extra_fields
        )

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password =None , **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('role' , 'super_user')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser field is_superuser must be True')

        return self.create_user(email=email, password=password, **extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):

    STUDENT = 'student'
    COUNSELOR = 'academic_counselor'
    COORDINATOR = 'review_coordinator'
    ADMIN = 'brototype_admin'
    SUPERUSER = 'super_user'

    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (COUNSELOR, 'Academic Counselor'),
        (COORDINATOR, 'Review Coordinator'),
        (ADMIN, 'Brototype Admin'),
        (SUPERUSER, 'Super User'),
    )
    
    fullname        = models.CharField(max_length=100, blank=True)
    email           = models.EmailField(max_length=200, unique=True, db_index=True, null=False)
    role            = models.CharField(default='student',max_length=200, choices=ROLE_CHOICES, blank=True)
    is_verified     = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=True)
    is_superuser    = models.BooleanField(default=False)
    is_block        = models.BooleanField(default=False)
    created_at      = models.DateField(auto_now_add=True)
    updated_at      = models.DateField(auto_now=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['fullname']

    objects = UserManager()

    def __str__(self):
        return self.fullname


class Badges(models.Model):
    badge_name = models.CharField(max_length=50)
    badge_icon = models.ImageField('badgeIcon')
    badge_desc = models.TextField()

    class Meta:
        verbose_name_plural = 'Badges'

    def __str__(self):
        return self.badge_name

class Hub(models.Model):
    location = models.CharField(max_length=50,unique=True)
    code     = models.CharField(max_length=6,unique=True)

    def __str__(self) -> str:
        return f'{self.location} ({self.code})'
    

class Batch(models.Model):
    hub = models.ForeignKey(Hub,on_delete=models.CASCADE)
    number = models.CharField(max_length=50,unique=True)

    class Meta:
        verbose_name_plural = 'batches'
    
    def get_name(self):
        return f'{self.hub.code}{self.number}'.upper()

    def __str__(self) -> str:
        return f'{self.hub.code}{self.number}'.upper()
    

class UserProfile(models.Model):
    user                 = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image        = models.ImageField(upload_to='profiles',null=True)
    about                = models.TextField(null=True)
    personal_website     = models.CharField(max_length=200,null=True)
    communication_cord   = models.BooleanField(default=False)
    tech_cord            = models.BooleanField(default=False)
    following_count      = models.PositiveIntegerField(default=0)
    followers_count      = models.PositiveIntegerField(default=0)
    is_profile_completed = models.BooleanField(default=False)
    badges               = models.ManyToManyField(Badges)
    hub                  = models.ForeignKey(Hub,on_delete=models.CASCADE,null=True)
    batch                = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.user.fullname

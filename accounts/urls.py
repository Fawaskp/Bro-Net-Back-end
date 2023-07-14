from django.urls import path
from .views import ViewUsers, ViewUserProfile

urlpatterns = [
    path('',ViewUsers.as_view()),
    path('profile/',ViewUserProfile.as_view()),
]

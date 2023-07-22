from django.urls import path
from .views.userViews import CombinedUserView

urlpatterns = [
    path('users/', CombinedUserView.as_view(), name='combined-users'),
]

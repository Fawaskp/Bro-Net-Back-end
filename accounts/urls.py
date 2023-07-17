from django.urls import path
from .views import ViewUsers, ViewUserProfile,LoginWithEmail,UserProfileDetail,\
MyTokenObtainPairView,GetHubList,GetBatchList,GetStackList,UserDetail

urlpatterns = [
    path('',ViewUsers.as_view()),
    path('token/',MyTokenObtainPairView.as_view()),
    path('profile/',ViewUserProfile.as_view()),
    path('login/email/',LoginWithEmail.as_view()),
    path('user/<int:id>/', UserDetail.as_view()),
    path('user-profile/<int:id>/', UserProfileDetail.as_view()),
    path('hub',GetHubList.as_view()),
    path('batch',GetBatchList.as_view()),
    path('stack',GetStackList.as_view()),
]

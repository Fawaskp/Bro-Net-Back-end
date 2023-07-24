from django.urls import path
from .viewslogin import LoginWithSocialMedia,LoginWithEmail,token
from .views import ViewUsers, ViewUserProfile,UserProfileDetail,\
GetHubList,GetBatchList,GetStackList,UserDetail
from .views2 import SkillView,SocialMediaView,AddSkill,ProjectView,UserSocialMediaAccountsView
from .viewslogin import check_username


urlpatterns = [
    path('',ViewUsers.as_view()),
    path('profile/',ViewUserProfile.as_view()),
    path('login/email/',LoginWithEmail.as_view()),
    path('login/social-media/',LoginWithSocialMedia.as_view()),
    path('user/<int:id>/', UserDetail.as_view()),
    path('user-profile/<int:id>/', UserProfileDetail.as_view()),
    path('hub',GetHubList.as_view()),
    path('batch',GetBatchList.as_view()),
    path('stack',GetStackList.as_view()),
    path('skill',SkillView.as_view()),
    path('add-skill/<int:id>/',AddSkill.as_view()),
    path('project/<int:id>/',ProjectView.as_view()),
    path('social-media',SocialMediaView.as_view()),
    path('user-social-media',UserSocialMediaAccountsView.as_view()),

    path('token/',token),
    path('check-username',check_username)
]

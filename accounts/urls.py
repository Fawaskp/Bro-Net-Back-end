from django.urls import path
from .viewslogin import LoginWithSocialMedia,LoginWithEmail,token,check_username,is_user_auth,is_su_auth
from .views import ViewUsers, ViewUserProfile,UserProfileDetail,\
GetHubList,GetBatchList,GetStackList,UserDetail
from .views2 import SkillView,SocialMediaView,AddSkill,ProjectViewSet,UserSocialMediaAccountsView,\
UserEducationView,WorkExperienceView,EducationCategoriesView


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
    path('project/<int:user_id>/',ProjectViewSet.as_view({'get':'list'})),
    path('social-media',SocialMediaView.as_view()),
    path('user-social-media',UserSocialMediaAccountsView.as_view()),
    path('education-categories',EducationCategoriesView.as_view()),
    path('user-education',UserEducationView.as_view()),
    path('user-work-experience',WorkExperienceView.as_view()),

    path('token/',token),
    path('check-username',check_username),
    path('is-user-auth',is_user_auth),
    path('is-su-auth',is_su_auth),
]

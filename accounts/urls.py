from django.urls import path
from .views_login import LoginWithSocialMedia,LoginWithEmail,token,check_username,is_user_auth,is_su_auth,get_user_id_by_username
from .views import SearchUser, ViewUserProfile,UserProfileDetail,\
GetHubList,GetBatchList,GetStackList,UserDetail
from .views2 import SkillView,SocialMediaView,SkillDetail,ProjectViewSet,UserSocialMediaAccountsView,\
UserEducationView,UserEducationDetail,WorkExperienceView,EducationCategoriesView


urlpatterns = [
    path('search/<int:user_id>/',SearchUser.as_view()),
    path('profile/',ViewUserProfile.as_view()),
    path('login/email/',LoginWithEmail.as_view()),
    path('login/social-media/',LoginWithSocialMedia.as_view()),
    path('user/<int:id>/', UserDetail.as_view()),
    path('user-profile/<int:id>/', UserProfileDetail.as_view()),

    path('hub',GetHubList.as_view()),
    path('batch',GetBatchList.as_view()),
    path('stack',GetStackList.as_view()),
    
    path('skill',SkillView.as_view()),
    path('user-skill-detail/<int:id>/',SkillDetail.as_view()),
    path('project/<int:user_id>/',ProjectViewSet.as_view({'get':'list'})),
    path('social-media',SocialMediaView.as_view()),
    path('user-social-media',UserSocialMediaAccountsView.as_view()),
    path('education-categories',EducationCategoriesView.as_view()),
    path('user-education',UserEducationView.as_view()),
    path('user-education-detail/<int:id>/',UserEducationDetail.as_view()),
    path('user-work-experience',WorkExperienceView.as_view()),

    path('token/',token),
    path('check-username',check_username),
    path('get-user-id/<str:username>/',get_user_id_by_username),
    path('is-user-auth',is_user_auth),
    path('is-su-auth',is_su_auth),
]

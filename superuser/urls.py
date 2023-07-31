from django.urls import path
from .views.userViews import StudetsView,CouncellorsView,AdminsView,CoOrdinatorsView,SkillsView,\
SocialMediaView,SocialMediaDetail,SkillsViewDetail,BadgesView,ProjectView,admin_login

urlpatterns = [
    path('students/', StudetsView.as_view()),
    path('councellors/', CouncellorsView.as_view()),
    path('admins/', AdminsView.as_view()),
    path('co-ordinator/', CoOrdinatorsView.as_view()),

    path('skills/', SkillsView.as_view()),
    path('skill/<int:id>/', SkillsViewDetail.as_view()),
    path('social-media/', SocialMediaView.as_view()),
    path('social-media/<int:id>/', SocialMediaDetail.as_view()),
    path('badges/', BadgesView.as_view()),
    path('projects/', ProjectView.as_view()),
    path('login',admin_login),

]

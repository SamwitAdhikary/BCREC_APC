from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="HomePage"),
    path('login/', views.loginUser, name="loginUser"),
    path('about/', views.about, name="AboutPage"),
    path('contact/', views.contact, name="ContactPage"),
    path('profile/', views.profile, name="profilePage"),
    path('logout/', views.logoutUser, name='logout'),
    path('overview/', views.overview, name="OverViewPage"),
    path('mission-and-overview/', views.mission_and_vision, name="MissionPage"),
    path('general-secretary-message/', views.general_secretary_message, name='GeneralSecretaryPage'),
    path('principals-message/', views.principal_message, name="PrincipalMessagePage"),
    path('approval-affiliation/', views.approval_affiliation, name="ApprovalAffiliationPage"),
    path('collaboration-mous/', views.collaboration, name="CollaborationPage"),
    path('committees/', views.committees, name="CommitteesPage")
]

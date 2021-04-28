from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="HomePage"),
    path('login/', views.loginUser, name="loginUser"),
    path('about/', views.about, name="AboutPage"),
    path('contact/', views.contact, name="ContactPage"),
    path('profile/', views.profile, name="profilePage"),
    path('verify-user/', views.verify_user, name="verifyUser"),
    path('verify-otp/<str:username>/<str:email>/<int:otp>/<str:password>/',
         views.verify_otp, name="verifyOTP"),

    path('reset-password', auth_views.PasswordResetView.as_view(template_name="home/reset-password.html"),
         name='reset_password'),
    path('reset-password-send', auth_views.PasswordResetDoneView.as_view(template_name="home/reset-password-send.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="home/reset-password-confirm.html"),
         name='password_reset_confirm'),
    path('reset-password-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="home/reset-password-complete.html"), name='password_reset_complete'),


    path('<str:pk>/update-profile/', views.update, name="UpdateProfile"),
    path('<str:pk>/update-image/', views.updateImage, name="UpdateImage"),
    path('logout/', views.logoutUser, name='logout'),
    path('overview/', views.overview, name="OverViewPage"),
    path('mission-and-overview/', views.mission_and_vision, name="MissionPage"),
    path('general-secretary-message/',
         views.general_secretary_message, name='GeneralSecretaryPage'),
    path('principals-message/', views.principal_message,
         name="PrincipalMessagePage"),
    path('approval-affiliation/', views.approval_affiliation,
         name="ApprovalAffiliationPage"),
    path('collaboration-mous/', views.collaboration, name="CollaborationPage"),
    path('committees/', views.committees, name="CommitteesPage")
]

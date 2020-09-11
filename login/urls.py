from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("reg",views.reg,name="reg"),
    path("success",views.success,name="success"),
    path("registration",views.registration,name="registration"),
    path("login_auth",views.login_auth,name="login_auth"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("profile_change",views.profile_change,name="profile_change"),
    path("profile_change_form",views.profile_change_form,name="profile_change_form"),
    path("text_check",views.text_check,name="text_check"),
    
    path("ajax_call",views.ajax_call,name="ajax_call")
]

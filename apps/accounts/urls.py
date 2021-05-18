from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('recuperar_contrasena/', views.forgotPassword, name='forgotPassword'),
    # resetpassword_validate
    path('resetpassword_validate/<uidb64>/<token>/',
         views.resetpassword_validate, name='resetpassword_validate'),
    path('reestablecer_contrasena/', views.resetPassword, name='resetPassword'),
]

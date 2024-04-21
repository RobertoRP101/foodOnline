from django.urls import path
from . import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),
    path('customerDashboard/', views.customerDashboard, name='customerDashboard'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPasswordValidate/<uidb64>/<token>', views.resetPasswordValidate, name='resetPasswordValidate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]

from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings  

urlpatterns = [
    path('', views.login_user, name='login'),  # This line handles /Login/
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register_user'),
    path('adminLogin', views.admin_login, name='adminLogin'),
    path('adminLogout', views.admin_logout, name='adminLogout'),
    path('payment/', views.payment_view, name='payment'),
    path('receipt/', views.receipt_view, name='receipt'),
    path('receipt/pdf/', views.receipt_pdf_view, name='receipt_pdf'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.urls import path
from . import views

  
urlpatterns = [
    path('dashboard/', views.index, name='dashboard_index'),
    path('adminDashboard/', views.admin_dashboard, name='admin_dashboard'),

    
]

'''
    path('AdvisorAchievement', views.advisorAchievement, name ="AdvisorAchievement")
'''
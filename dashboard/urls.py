from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:pk>', views.project_detail, name='project_detail'),

]

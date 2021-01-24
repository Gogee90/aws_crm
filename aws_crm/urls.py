from django.urls import path
from . import views


urlpatterns = [
    path('createenv/', views.create_environment, name='create_environment'),
    path('createapp/', views.create_application, name='create_application'),
    path('envs/', views.get_all_envs, name='get_all_envs'),
    path('envs/<str:id>', views.retrieve_single_env, name='retrieve_single_env'),
    path('restartenv/<str:id>', views.restart_server, name="restart_server"),
    path('terminateenv/<str:id>', views.terminate_env, name="terminate_env"),
    path('updateapp/', views.update_application, name='update_application'),
    path('', views.login_user, name='login')
]

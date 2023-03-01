from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, TareasView, TareaDeleteView, TareaEditarView, SingUpView, CustomLoginView


app_name = 'todo'

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),
    path('task/create/', TareasView.as_view(), name = 'taskcreate'),
    path('eliminar/<int:pk>', TareaDeleteView.as_view(), name= 'delete'),
    path('update/<int:pk>', TareaEditarView.as_view(), name='update'),

    ]
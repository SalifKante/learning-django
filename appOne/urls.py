from django.urls import path
from appOne import views



urlpatterns = [
    path('', views.index, name="index"),
    path('record_list', views.record_list, name="record_list"),
    path('users', views.get_user, name="users"),
    path('create_user', views.create_user, name="create_user"),
    path('form_page', views.form_name_view, name="form_name_view"),
    path('register', views.register, name="register"),
    path('user_login', views.user_login, name='user_login'),
]

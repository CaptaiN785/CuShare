from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='server'),
    path('manage/', views.manage_server, name='server-manage'),
    path('create/', views.create_server, name='server-create'),
    path("upload/", views.upload, name='server-upload'),
    path('delete/<str:id>', views.delete, name='server-delete'),
    path('login/', views.login, name='server-login'),
    path('code/<str:code_id>', views.code, name="server-code"),
    path('codelist/<server_id>', views.code_list, name='server-code-list'),
    path('deleteserver', views.delete_server, name='delete-server'),
    path('changepassword', views.change_password, name='changepassword'),
]
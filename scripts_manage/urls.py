from django.urls import path
from scripts_manage import views


urlpatterns = [
    path('register_script/', views.register_script_view, name='register_script'),
    path('script_list/', views.scripts_list_view, name='script_list'),
    path('get_modify_script/<script_id>', views.script_modify_view, name='get_modify_script'),
    path('script_details/<script_id>', views.script_details_view, name='script_details'),
    path('script_del/', views.del_script_view, name='script_del'),
]

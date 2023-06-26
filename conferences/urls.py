from django.urls import path
from conferences import views

urlpatterns = [
    path('', views.conf_list, name = "Home_View"),
    path('add_conf/', views.conf_add, name='conf_add'),
    path('details/<int:id>', views.details, name="Deatails"),
    # path('conferences/<id>/update', views.update_conference_view),
    # path('conferences/<id>/delete', views.delete_conference_view),
    # path('conferences/<id>/delete-confirm', views.confirm_delete_view)
]
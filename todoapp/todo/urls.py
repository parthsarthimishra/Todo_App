from django.urls import path

from .views import index, detail, create ,edit, delete_item , create_item , edit_list , delete_list

app_name='todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('create/', create, name='list_create'),
    path('<int:list_id>/edit/<int:item_id>/',edit,name='item_edit'),
    path('<int:list_id>/delete/<int:item_id>/',delete_item,name='item_delete'),
    path('<int:list_id>/create/',create_item,name='item_create'),
    path('edit/<int:list_id>/', edit_list, name='list_edit'),
    path('delete/<int:list_id>/',delete_list,name='list_delete'),
]
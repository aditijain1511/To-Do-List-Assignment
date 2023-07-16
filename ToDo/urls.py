
from django.contrib import admin
from django.urls import path
from toDo_list import views
 
urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('updatedTask/<str:item_id>', views.updatedTask, name="updatedTask"),
    path('admin/', admin.site.urls),
]
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('addTodo', views.addTodo, name='title'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
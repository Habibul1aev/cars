from django.urls import path
from workspace import views


urlpatterns = [
    path('', views.main, name='workspace'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update')
]
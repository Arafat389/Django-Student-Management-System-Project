from django.urls import path
from .views import student_register, student_list, student_update, student_delete

urlpatterns = [
    path('register/', student_register, name='student_register'),
    path('list/', student_list, name='student_list'),
    path('update/<int:pk>/', student_update, name='student_update'),
    path('delete/<int:pk>/', student_delete, name='student_delete'),
]

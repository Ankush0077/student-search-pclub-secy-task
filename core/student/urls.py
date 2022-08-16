from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_search, name='student-search'),
    path('family/<int:roll_no>', views.family_tree, name='family-tree'),
]
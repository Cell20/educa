from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users_detail'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),

    path('', include(router.urls)),
]

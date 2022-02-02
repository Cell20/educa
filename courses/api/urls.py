from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='courses')
router.register('subjects', views.SubjectViewSet, basename='subjects')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

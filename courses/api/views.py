from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer
from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    query_set = Subject.objects.all()
    serializer_class = SubjectSerializer

    # """Why not ModelViewSet? - MVS provides both a list & detail view for us.
    # ReadOnlyModelViewSet provides read-only actions to both list obj and
    # retrieves a single obj. | Basically, a ReadOnly Version of ModelViewSet."""


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    # detail=True to specify an action to be performed on a single obj.

    @action(detail=True, methods=['get'], serializer_class=CourseWithContentsSerializer, authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# class CourseEnrollView(APIView):
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})

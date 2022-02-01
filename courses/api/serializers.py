from rest_framework import serializers
from ..models import Subject, Course, Module
from django.contrib.auth import get_user_model

# from courses.models import Subject
# from courses.api.serializers import SubjectSerializer
# subject = Subject.objects.latest('id')
# serializer = SubjectSerializer(subject)
# serializer.data


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('id', 'username', 'email')


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializer(serializers.ModelSerializer):
    # many=True to indicate that we're serializing multiple obj. read_only to indicate this field is read only
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules']

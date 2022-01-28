from rest_framework import serializers
from ..models import Subject

# from courses.models import Subject
# from courses.api.serializers import SubjectSerializer
# subject = Subject.objects.latest('id')
# serializer = SubjectSerializer(subject)
# serializer.data

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']

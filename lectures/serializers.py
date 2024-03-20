from rest_framework import serializers
from .models import Student, Teacher, Lecture, LectureHistory

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = '__all__'


class LectureHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LectureHistory
        fields = '__all__'

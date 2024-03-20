# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random

from .models import Subject, Student, Teacher, Lecture, LectureHistory
from .serializers import StudentSerializer, TeacherSerializer, LectureSerializer , LectureHistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# def data(request):
    # return HttpResponse("here is your response from the server hehe - ej")

def random_data(request, num):
    data = []
    for _ in range(num):
        data.append(sorted(random.sample(range(1, 45), 6)))

    return JsonResponse(data, safe=False)

def json_data(request):
    data = {'name':'ej', 'age':18, 'city':'Seoul'}
    return JsonResponse(data)


# 1. create는 django seed로 함

# 2-1. read(전체) 하기

# 강좌 전체
@api_view(['GET'])
def read_lectures(request):
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

# 강좌 수강내역 전체
def read_lectureshistory(request):
    lectures_history = LectureHistory.objects.all()
    return HttpResponse(lectures_history)

# 2-2. read(하나) 하기

# 강좌 id별
def read_lectures_id(request, id):
    lectures = Lecture.objects.get(id=id)
    return HttpResponse(lectures)

# 강좌 수강내역 id별
def read_lectureshistory_id(request, id):
    lectures_history = LectureHistory.objects.get(id=id)
    return HttpResponse(lectures_history)


# 2-3. read(필터링) 하기

# 강좌 교과목별

def read_lectures_sbj(request):
    lectures = Lecture.objects.filter(subject_id=15)
    # json 형태로 바꾸면 좋겠지만? 일단 pass
    return HttpResponse(lectures)

# 강좌 강사별
def read_lectures_tch(request):
    lectures = Lecture.objects.filter(teacher_id=7)
    return HttpResponse(lectures)

# 강좌 수강내역 강좌별
def read_lectureshistory_lec(request):
    lectures_history = LectureHistory.objects.filter(lecture_id=3)
    return HttpResponse(lectures_history)

# 강좌 수강내역 학생별
def read_lectureshistory_stu(request):
    lectures_history = LectureHistory.objects.filter(student_id=9)
    return HttpResponse(lectures_history)



# 3. api_view 하기

# 강좌 전체 조회
@api_view(['GET'])
def lecture_list(request):
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

# 강좌 id별 조회
@api_view(['GET'])
def lecture_detail(request, pk):
    lecture = Lecture.objects.get(id=pk)
    serializer = LectureSerializer(lecture)
    return Response(serializer.data)

# 학생 전체 조회
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# 강사 전체 조회
@api_view(['GET'])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)










# 1.  create 하기

# def create(request):
#     subject = Subject(title="ENGLISH")
#     subject.save()
    
#     return HttpResponse(subject)

# def create(request):
#     student = Student(name="eunji")
#     student.save()
    
#     return HttpResponse(student)

# def create(request):
#     teacher = Teacher(name="Lee")
#     teacher.save()
    
#     return HttpResponse(teacher)

# def create(request):
#     lecture = Lecture(name="best lecture")
#     lecture.save()

#     return HttpResponse(lecture)

# def create(request):
#     lecture_history = LectureHistory()
#     lecture_history.save()

#     return HttpResponse(lecture_history)


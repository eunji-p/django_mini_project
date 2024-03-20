from django.db import models

# Create your models here.

# 변수명은 소문자로, 모델명은 class니까 대문자로 시작

class Subject(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.id}: {self.title}"

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    signup_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    lecture_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Student(models.Model):
    name = models.CharField(max_length=50)
    signup_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}: {self.name}"


class Lecture(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    introduction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.name}"

    # CharField 는 길이 제한이 있는 문자열 필드
    # 여기서는 강좌명
    # content = models.TextField()
    # TextField는 길이 제한이 없는 문자열 필드
    # 여기서는 강좌소개


class LectureHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now_add=True)
    test_score = models.FloatField()

    # def __str__(self):
    #     return f"{self.id}: {self.title}"


# 안 써도 됨 (예쁘게 보여주는 용도)
    # def __str__(self):
    #     return f"{self.id}: {self.title}"
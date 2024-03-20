from django.urls import path
from lectures import views

urlpatterns = [
    # path('', views.data),
    path('json-data/', views.json_data),
    path("random-data/<int:num>/", views.random_data),

# 조회: 강좌(전체/id별/과목별/강사별), 강좌 수강내역(전체/id별/강좌별/학생별)
    path('read/lecture/', views.read_lectures),
    path('read/lecture/<int:id>/', views.read_lectures_id),
    path('read/lecture/sbj/', views.read_lectures_sbj),
    path('read/lecture/tch/', views.read_lectures_tch),
    path('read/lecturehistory/', views.read_lectureshistory),
    path('read/lecturehistory/<int:id>/', views.read_lectureshistory_id),
    path('read/lecturehistory/lec/', views.read_lectureshistory_lec),
    path('read/lecturehistory/stu/', views.read_lectureshistory_stu),

# 조회: 강좌, 학생, 강사
    path("lecture_list/", views.lecture_list),
    path("lecture_detail/<int:pk>/", views.lecture_detail),
    path("student_list/", views.student_list),
    # path("student_detail/<int:pk>/", views.student_detail),
    path("teacher_list/", views.teacher_list),


]





    # # path('',views.subject_list),
    # # subject-list/ lectures(url), subject(model)이라 원래 안 맞는데.. 일단 함
    # path('<int:pk>/', views.subject_detail),
    # path('create/', views.create),
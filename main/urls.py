from django.urls import path
from main.views import  *

app_name = 'main'

urlpatterns = [
    path('', show_main, name="main"),

    path('api/kelompok/get/', get_kelompok, name="get_kelompok"),
    path('api/mentor/get/', get_mentor, name="get_mentors"),
    path('api/acara/get/', get_acara, name="get_acara"),
    path('api/PI/get/', get_PI, name="get_PI"),
    path('api/BPH/get/', get_BPH, name="get_BPH"),
    path('api/panitia/get/', get_panitia, name="get_panitia"),
    path('api/mentee/get/', get_mentee, name="get_mentee"),
    path('api/mentoring/get/<int:kelompok>/', get_mentoring, name="get_mentoring"),
    path('api/rapat/get/<int:divisi>/', get_rapat, name="get_rapat"),
    path('api/sponsor/get/', get_sponsor, name="get_sponsor"),
    path('api/kelompok/get/', post_kelompok, name="post_kelompok"),
    path('api/acara/post/', post_acara, name="post_acara"),
    path('api/mentee/post/', post_mentee, name="post_mentee"),
    path('api/PI/post/', post_PengurusInti, name="post_PI"),
    path('api/mentor/post/', post_mentor, name="post_mentor"),
    path('api/BPH/post/', post_BPH, name="post_BPH"),
    path('api/mentoring/post/', post_mentoring, name="post_mentoring"),
    path('api/rapat/post/', post_rapat, name="post_rapat"),
    path('api/sponsor/post/', post_sponsor, name="post_sponsor"),
    path('api/hadir-mentoring/put/', hadir_mentoring, name="hadir_mentoring"),
    path('api/add-pembicara/put/', add_pembicara, name="add_pembicara"),
    path('api/acara/put/<str:acara>/', put_acara, name="put_acara"),
    path('api/mentor/put/<str:npm>/', put_mentor, name="put_mentor"),
    path('api/mentee/put/<str:npm>/', put_mentee, name="put_mentee"),
    path('api/acara/delete/<str:acara>/', delete_acara, name="put_acara"),
    path('api/mentor/delete/<str:npm>/', delete_mentor, name="delete_mentor"),
    path('api/mentee/delete/<str:npm>/', delete_mentee, name="delete_mentee"),
]
from django.urls import path
from main.views import  *

app_name = 'main'

urlpatterns = [
    path('', show_main, name="main"),
    path('api/acara/', acara, name="acara"),
    path('api/acara/<str:acara>/', acara_by_id, name="acara_by_id"),
    path('api/kelompok/', kelompok, name="kelompok"),
    path('api/bph/', bph, name="bph"),
    path('api/bph/<str:npm>/', bph_by_id, name="bph_by_id"),
    path('api/mentor/', mentor, name="mentor"),
    path('api/mentor/<str:npm>/', mentor_by_id, name="mentor_by_id"),
    path('api/mentee/', mentee, name="mentee"),
    path('api/mentee/<str:npm>/', mentee_by_id, name="mentee_by_id"),
    path('api/sponsor/', sponsor, name="sponsor"),
    path('api/sponsor/<str:acara>/<str:perusahaan>/', sponsor_by_id, name="sponsor_by_id"),
    path('api/mentoring/', mentoring, name="mentoring"),
    path('api/mentoring/<int:kelompok>/', mentoring_by_kelompok, name="mentoring_by_kelompok"),
    path('api/mentoring/<int:kelompok>/<str:materi>/', mentoring_by_kelompok_materi, name="mentoring_by_kelompok_materi"),
    path('api/rapat/',rapat, name="rapat"),
    path('api/rapat/<str:divisi>/', rapat_by_divisi, name="rapat_by_divisi"),
    path('api/hadir-mentoring/<int:kelompok>/<str:materi>/', hadir_mentoring, name="hadir_mentoring"),
    path('api/add-pembicara/<str:acara>/', add_pembicara, name="add_pembicara"),
    path('api/pi/',pengurusInti , name="pengurus_inti"),
    path('api/pi/<str:npm>/', PI_by_id, name="pi_by_id"),
    path('api/panitia/', panitia, name="panitia"),

]
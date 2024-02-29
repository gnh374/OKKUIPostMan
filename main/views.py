from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from main.forms import *

def show_main(request):  
    return render(request, "postman.html")


@csrf_exempt
def post_acara(request):
    if request.method == 'POST':
            try:
                json_input = json.loads(request.body)
                nama = json_input.get("nama")
                tempat = json_input.get("tempat")
                waktu_mulai = datetime.strptime(json_input.get("waktu_mulai"), "%Y-%m-%dT%H:%M:%S")
                waktu_selesai = datetime.strptime(json_input.get("waktu_selesai"), "%Y-%m-%dT%H:%M:%S")
                acara = Acara(nama=nama, tempat=tempat, waktu_mulai=waktu_mulai, waktu_selesai=waktu_selesai)
                acara.save()
                return HttpResponse(serializers.serialize('json', [acara]))
            except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
        
@csrf_exempt
def post_PengurusInti(request):
    if request.method == 'POST':
            try:
                json_input = json.loads(request.body)
                nama = json_input.get("nama")
                fakultas = json_input.get("fakultas")
                angkatan = json_input.get("angkatan")
                jurusan = json_input.get("jurusan")
                divisi = DivisiPI(nama=json_input.get("divisi"))
                pengurus_inti = PengurusInti(nama=nama, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, divisi=divisi)
                pengurus_inti.save()
                return HttpResponse(serializers.serialize('json', [pengurus_inti])) 
            except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405) 
        

@csrf_exempt
def post_kelompok(request):
    kelompok = Kelompok()
    kelompok.save()
    return HttpResponse(serializers.serialize('json', [kelompok]))



@csrf_exempt
def post_BPH(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            divisi = DivisiBPH(nama=json_input.get("divisi")) 
            jabatan = json_input.get("jabatan")
            if (jabatan=="PJ" and BPH.objects.filter(divisi=divisi, jabatan="PJ").exists()):
                pass
            elif(jabatan=="WaPJ" and BPH.objects.filter(divisi=divisi, jabatan="WaPJ").count() == 2):
                pass
            else:
                bph = BPH(nama=nama, fakultas=fakultas, angkatan=angkatan,jurusan=jurusan, divisi=divisi, jabatan=jabatan)
                bph.save()
                return HttpResponse(serializers.serialize('json', [bph]))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)    
    
@csrf_exempt
def post_mentor(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            mentor = Mentor(nama=nama, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, kelompok=kelompok)
            mentor.save()
            return HttpResponse(serializers.serialize('json', [mentor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
    
@csrf_exempt
def post_mentee(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            jalur_masuk = json_input.get("jalur_masuk")
            mentee = Mentee(nama=nama, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, kelompok=kelompok, jalur_masuk=jalur_masuk)
            mentee.save()
            return HttpResponse(serializers.serialize('json', [mentee]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def post_sponsor(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            acara =  Acara.objects.get(pk=json_input.get("acara"))
            perusahaan = Perusahaan.objects.get(pk=json_input.get("perusahaan")) 
            paket = json_input.get("paket")
            sponsor = Sponsor(acara=acara, paket=paket, perusahaan=perusahaan)
            sponsor.save()
            return HttpResponse(serializers.serialize('json', [sponsor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def post_mentoring(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            waktu =  datetime.strptime(json_input.get("waktu"), "%Y-%m-%dT%H:%M:%S")
            tempat = json_input.get("tempat")
            materi = json_input.get("materi")
            mentoring = Mentoring(kelompok=kelompok, waktu=waktu,tempat=tempat, materi=materi)
            mentoring.save()
            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def post_rapat(request):
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            divisi = DivisiBPH.objects.get(pk= json_input.get("divisi"))
            waktu =  datetime.strptime(json_input.get("waktu"), "%Y-%m-%dT%H:%M:%S")
            tempat = json_input.get("tempat")
            kesimpulan = json_input.get("kesimpulan")
            rapat = Mentoring(divisi=divisi, waktu=waktu,tempat=tempat, kesimpulan=kesimpulan)
            rapat.save()
            return HttpResponse(serializers.serialize('json', [rapat]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def hadir_mentoring(request):
    if request.method == 'PUT':
        try:
            json_input = json.loads(request.body)
            npm = json_input.get("npm")
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            materi = json_input.get("materi")
            mentoring = Mentoring.objects.get(kelompok=kelompok, materi=materi)
            mentee = Mentee.objects.get(npm=npm, kelompok=kelompok)
            mentoring.hadir.add(mentee)
            mentoring.save()
            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def add_pembicara(request):
    if request.method == 'PUT':
        try:
            json_input = json.loads(request.body)
            pembicara = Pembicara.objects.get(pk=json_input.get("pembicara"))
            acara= Acara.objects.get(pk=json_input.get("acara"))
            acara.pembicara.add(pembicara)
            acara.save()
            return HttpResponse(serializers.serialize('json', [acara]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def get_PI(request):
    PI = PengurusInti.objects.all()
    return HttpResponse(serializers.serialize('json', PI))

def get_mentoring(request, kelompok):
    kelompok = Kelompok.objects.get(pk=kelompok)
    mentoring= kelompok.mentoring.all()
    return HttpResponse(serializers.serialize('json', mentoring))

def get_rapat(request, divisi):
    divisi = DivisiBPH.objects.get(pk=divisi)
    rapat= divisi.rapat.all()
    return HttpResponse(serializers.serialize('json', rapat))

def get_BPH(request):
    BPH = PengurusInti.objects.all()
    return HttpResponse(serializers.serialize('json', BPH))
    
def get_sponsor(request):
    sponsor = Sponsor.objects.all()
    return HttpResponse(serializers.serialize('json',sponsor))

def get_acara(request):
    acara = Acara.objects.all()
    return HttpResponse(serializers.serialize('json', acara))

def get_mentor(request):
    mentors = Mentor.objects.all()
    return HttpResponse(serializers.serialize('json', mentors))

def get_mentor_by_kelompok(request, nomorKelompok):
    kelompok = Kelompok.objects.get(pk=nomorKelompok)
    mentor = Mentor.objects.get(kelompok=kelompok)
    return HttpResponse(serializers.serialize('json', mentor))


def get_kelompok(request):
    kelompok = Kelompok.objects.all()
    return HttpResponse(serializers.serialize('json', kelompok))

def get_panitia(request):
    panitia= Panitia.objects.all()
    return HttpResponse(serializers.serialize('json', panitia))

def get_pengurus_inti(request):
    pengurus_inti = PengurusInti.objects.all()
    return HttpResponse(serializers.serialize('json', pengurus_inti))

def get_BPH(request):
    bph= BPH.objects.all()
    return HttpResponse(serializers.serialize('json', bph))

def get_mentee(request):
    bph= Mentee.objects.all()
    return HttpResponse(serializers.serialize('json', bph))

@csrf_exempt
def put_acara(request,acara):
    if request.method == 'PUT':
        try:
            acara = Acara.objects.get(pk=acara)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if hasattr(Acara(), key):
                    list_change.append(key)
                     
            for attribute in list_change:
                setattr(acara, attribute, json_input.get(attribute))

            acara.save()
            return HttpResponse(serializers.serialize('json', [acara]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
@csrf_exempt
def put_mentor(request,acara):
    if request.method == 'PUT':
        try:
            mentor = Mentor.objects.get(pk=acara)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            # fields = Acara._meta.get_fields()
            # attribute_names = [field.name for field in fields]
            for key in keys:
                if hasattr(Mentor(), key):
                    list_change.append(key)
                     
            for attribute in list_change:
                setattr(mentor, attribute, json_input.get(attribute))

            mentor.save()
            return HttpResponse(serializers.serialize('json', [mentor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def put_mentee(request,npm):
    if request.method == 'PUT':
        try:
            mentee= Mentee.objects.get(pk=npm)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if hasattr(Mentee(), key):
                    list_change.append(key)
                     
            for attribute in list_change:
                setattr(mentee, attribute, json_input.get(attribute))

            mentee.save()
            return HttpResponse(serializers.serialize('json', [mentee]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def delete_acara(request,acara):
    if request.method == 'DELETE':
        try:
            Acara.objects.get(pk=acara).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def delete_mentor(request,npm):
    if request.method == 'DELETE':
        try:
            Mentor.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def delete_mentee(request,npm):
    if request.method == 'DELETE':
        try:
            Mentee.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
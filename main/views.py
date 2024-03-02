
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from main.forms import *
from dateutil.parser import isoparse

def show_main(request):  
    return render(request, "postman.html")

@csrf_exempt
def acara_by_id(request,acara):
    if request.method == 'PUT':
        try:
            acara = Acara.objects.get(pk=acara)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if key =="nama":
                    raise Exception("Tidak bisa mengganti Nama Acara")
                if hasattr(Acara, key):
                    list_change.append(key)
                     
            for attribute in list_change:
                if attribute=="pembicara":
                    acara.pembicara.set(json_input.get(attribute))
                elif attribute=="waktu_mulai" or attribute=="waktu_selesai":
                    setattr(acara, attribute, isoparse(json_input.get(attribute)))
                else : 
                    setattr(acara, attribute, json_input.get(attribute))
            acara.save()
            return HttpResponse(serializers.serialize('json', [acara]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            Acara.objects.get(pk=acara).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def acara(request):
    if request.method=='GET':
        acara = Acara.objects.all()
        return HttpResponse(serializers.serialize('json', acara))
    elif request.method == 'POST':
            try:
                json_input = json.loads(request.body)
                nama = json_input.get("nama")
                if nama is None:
                    raise Exception("Nama acara tidak boleh kosong")
                elif Acara.objects.filter(nama=nama).exists():
                    raise Exception("Nama acara sudah ada")
                tempat = json_input.get("tempat")
                waktu_mulai = isoparse(json_input.get("waktu"))
                waktu_selesai = isoparse(json_input.get("waktu"))
                pembicara=json_input.get("pembicara")

                acara = Acara( nama=nama, tempat=tempat, waktu_mulai=waktu_mulai, waktu_selesai=waktu_selesai)
                acara.save()
                acara.pembicara.set(pembicara)

                return HttpResponse(serializers.serialize('json', [acara]))
            except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
 

@csrf_exempt
def kelompok(request):
    if request.method=='GET':
        kelompok = Kelompok.objects.all()
        return HttpResponse(serializers.serialize('json', kelompok))
    elif request.method=='POST':
        kelompok = Kelompok()
        kelompok.save()
        return HttpResponse(serializers.serialize('json', [kelompok]))
    return JsonResponse({"error": "Method not allowed"}, status=405)
    

@csrf_exempt
def bph(request):
    if request.method=='GET':
        bph = BPH.objects.all()
        return HttpResponse(serializers.serialize('json', bph))
    elif request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            npm = json_input.get("npm")
            if npm is None:
                raise Exception("NPM tidak boleh kosong")
            elif Mahasiswa.objects.filter(npm=npm).exists():
                    raise Exception("NPM sudah ada")
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            divisi = DivisiBPH(nama=json_input.get("divisi")) 
            jabatan = json_input.get("jabatan")
            if (jabatan!="PJ" and jabatan!="WaPJ" and jabatan!="Staff"):
                raise Exception("Jabatan tidak valid")

            if (jabatan=="PJ" and BPH.objects.filter(divisi=divisi, jabatan="PJ").exists()):
                raise Exception("Divisi ini sudah memiliki PJ")
            elif(jabatan=="WaPJ" and BPH.objects.filter(divisi=divisi, jabatan="WaPJ").count() == 2):
                raise Exception("Divisi ini sudah memiliki 2 WaPJ")
            else:
                bph = BPH(nama=nama, npm=npm, fakultas=fakultas, angkatan=angkatan,jurusan=jurusan, divisi=divisi, jabatan=jabatan)
                bph.save()
                return HttpResponse(serializers.serialize('json', [bph]))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)    

@csrf_exempt
def bph_by_id(request,npm):
    if request.method == 'PUT':
        try:
            bph = BPH.objects.get(pk=npm)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            divisi=bph.divisi
            list_change=[]
            for key in keys:
                if key=="npm":
                    raise Exception("Tidak bisa menggani NPM")
                if hasattr(BPH, key):
                    list_change.append(key)

            if "divisi" in list_change:
                divisi=json_input.get("divisi")  
                   
            for attribute in list_change:
                if attribute=="jabatan":
                    if json_input.get(attribute)!="PJ" and json_input.get(attribute)!="WaPJ"and json_input.get(attribute)!="Staff":
                        raise Exception("Jabatan tidak valid")
                    if json_input.get(attribute)=="PJ" and BPH.objects.filter(divisi=divisi, jabatan="PJ").exists():
                        raise Exception("Divisi ini sudah memiliki PJ")    
                    elif json_input.get(attribute)=="WaPJ" and BPH.objects.filter(divisi=divisi, jabatan="WaPJ").count() == 2:
                        raise Exception("Divisi ini sudah memiliki 2 WaPJ") 
                if attribute=="divisi":
                    setattr(bph, attribute, DivisiBPH.objects.get(pk=json_input.get(attribute)))
                setattr(bph, attribute, json_input.get(attribute))

            bph.save()
            return HttpResponse(serializers.serialize('json', [bph]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            BPH.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)



    
@csrf_exempt
def mentor(request):
    if request.method=='GET':
        mentors = Mentor.objects.all()
        return HttpResponse(serializers.serialize('json', mentors))
    elif request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            npm=json_input.get("npm")
            if npm is None:
                raise Exception("NPM tidak boleh kosong")
            elif Mahasiswa.objects.filter(npm=npm).exists():
                raise Exception("NPM sudah ada") 
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            mentor = Mentor(nama=nama, npm=npm, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, kelompok=kelompok)
            mentor.save()
            return HttpResponse(serializers.serialize('json', [mentor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def mentor_by_id(request,npm):
    if request.method == 'PUT':
        try:
            mentor = Mentor.objects.get(pk=npm)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if key =="npm":
                    raise Exception("Tidak bisa mengganti NPM")
                elif hasattr(Mentor, key):
                    list_change.append(key)
                     
            for attribute in list_change:
                if attribute=="kelompok":
                    setattr(mentor, attribute, Kelompok.objects.get(pk=json_input.get(attribute)))
                else:setattr(mentor, attribute, json_input.get(attribute))

            mentor.save()
            return HttpResponse(serializers.serialize('json', [mentor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            Mentor.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def mentee_by_id(request,npm):
    if request.method == 'PUT':
        try:
            mentee= Mentee.objects.get(pk=npm)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if key=="npm":
                    raise Exception("Tidak bisa mengganti NPM")
                if hasattr(Mentee, key):
                    list_change.append(key)
                     
            for attribute in list_change:
                if attribute=="kelompok":
                    setattr(mentee, attribute, Kelompok.objects.get(pk=json_input.get(attribute)))
                else:setattr(mentee, attribute, json_input.get(attribute))


            mentee.save()
            return HttpResponse(serializers.serialize('json', [mentee]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            Mentee.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def mentee(request):
    if request.method=='GET':
        mentee= Mentee.objects.all()
        return HttpResponse(serializers.serialize('json', mentee))
    elif request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            nama = json_input.get("nama")
            fakultas = json_input.get("fakultas")
            angkatan = json_input.get("angkatan")
            jurusan = json_input.get("jurusan")
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            jalur_masuk = json_input.get("jalur_masuk")
            npm=json_input.get("npm")
            if npm is None:
                raise Exception("NPM tidak boleh kosong")
            elif Mahasiswa.objects.filter(npm=npm).exists():
                raise Exception("NPM sudah ada")
            mentee = Mentee(nama=nama,npm=npm, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, kelompok=kelompok, jalur_masuk=jalur_masuk)
            mentee.save()
            return HttpResponse(serializers.serialize('json', [mentee]))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def sponsor(request):
    if request.method=='GET':
        sponsor = Sponsor.objects.all()
        return HttpResponse(serializers.serialize('json',sponsor))
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            acara =  Acara.objects.get(pk=json_input.get("acara"))
            perusahaan = Perusahaan.objects.get(pk=json_input.get("perusahaan")) 
            paket = json_input.get("paket")
            if (paket!="Gold" and paket!="Platinum" and paket!="Silver"):
                raise Exception("Paket tidak valid")
            
            sponsor = Sponsor(acara=acara, paket=paket, perusahaan=perusahaan)
            sponsor.save()
            return HttpResponse(serializers.serialize('json', [sponsor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def sponsor_by_id(request,acara, perusahaan):
    if request.method == 'PUT':
        try:
            acara = Acara.objects.get(pk=acara)
            perusahaan = Perusahaan.objects.get(pk=perusahaan)
            sponsor= Sponsor.objects.get(acara=acara, perusahaan=perusahaan)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if hasattr(Sponsor, key):
                    list_change.append(key)
                     
            for attribute in list_change:
                if attribute=="acara":
                    setattr(sponsor, attribute, Acara.objects.get(pk=json_input.get(attribute)) )
                elif attribute=="perusahaan":
                    setattr(sponsor, attribute, Perusahaan.objects.get(pk=json_input.get(attribute)) )
                if (attribute=="paket" and json_input.get(attribute)!="Gold" and json_input.get(attribute)!="Silver" and json_input.get(attribute)!="Platinum"):
                    raise Exception("Paket tidak valid")
                else:setattr(sponsor, attribute, json_input.get(attribute))

            sponsor.save()
            return HttpResponse(serializers.serialize('json', [sponsor]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            acara = Acara.objects.get(pk=acara)
            perusahaan = Perusahaan.objects.get(pk=perusahaan)
            sponsor= Sponsor.objects.get(acara=acara, perusahaan=perusahaan).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def mentoring(request):
    if request.method=='GET':
        mentoring = Mentoring.objects.all()
        return HttpResponse(serializers.serialize('json', mentoring))
    elif request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            kelompok = Kelompok.objects.get(pk= json_input.get("kelompok"))
            waktu = isoparse(json_input.get("waktu"))
            tempat = json_input.get("tempat")
            materi = json_input.get("materi")
            mentoring = Mentoring(kelompok=kelompok, waktu=waktu,tempat=tempat, materi=materi)
            mentoring.save()
            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def mentoring_by_kelompok(request, kelompok):
    if request.method=="GET":
        kelompok = Kelompok.objects.get(pk=kelompok)
        mentoring= kelompok.mentoring.all()
        return HttpResponse(serializers.serialize('json', mentoring))
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def mentoring_by_kelompok_materi(request, kelompok, materi):
    if request.method=='PUT':
        try:
            kelompok = Kelompok.objects.get(pk=kelompok)
            mentoring = Mentoring.objects.get(kelompok=kelompok, materi=materi)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if hasattr(Mentoring, key):
                    list_change.append(key) 

            for attribute in list_change:
                if(attribute=="kelompok"):
                    setattr(mentoring, attribute, Kelompok.objects.get(pk=json_input.get(attribute)) )
                elif(attribute=="waktu"):
                    setattr(mentoring, attribute,isoparse(json_input.get("waktu")))
                elif (attribute=="hadir"):
                    mentoring.hadir.set(json_input.get(attribute))
                else:setattr(mentoring, attribute, json_input.get(attribute))
            mentoring.save()

            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method=='DELETE':
        try:
            kelompok = Kelompok.objects.get(pk=kelompok)
            mentoring = Mentoring.objects.get(kelompok=kelompok, materi=materi).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def rapat(request):
    if request.method=="GET":
        rapat = Rapat.objects.all()
        return HttpResponse(serializers.serialize('json', rapat))
    elif request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            divisi = DivisiBPH.objects.get(pk= json_input.get("divisi"))
            waktu =  isoparse(json_input.get("waktu"))
            tempat = json_input.get("tempat")
            kesimpulan = json_input.get("kesimpulan")
            hadir=json_input.get("hadir")
            rapat = Rapat(divisi=divisi, waktu=waktu,tempat=tempat, kesimpulan=kesimpulan)
            rapat.save()
            rapat.hadir.set(hadir)
            
            return HttpResponse(serializers.serialize('json', [rapat]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def rapat_by_divisi(request, divisi):
    divisi = DivisiBPH.objects.get(pk=divisi)
    rapat= divisi.rapat.all()
    return HttpResponse(serializers.serialize('json', rapat))


@csrf_exempt
def hadir_mentoring(request, kelompok, materi):
    # if request.method == 'GET':
    #     mentoring = Mentoring.objects.get(kelompok=Kelompok.objects.get(pk=kelompok), materi=materi)
    #     concrete_model = mentoring._meta.concrete_model
    #     hadir = concrete_model.hadir
    #     return HttpResponse(serializers.serialize('json', [hadir]))

    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            npm = json_input.get("npm")
            kelompok = Kelompok.objects.get(pk=kelompok)
            mentoring = Mentoring.objects.get(kelompok=kelompok, materi=materi)
            mentee = Mentee.objects.get(npm=npm, kelompok=kelompok)
            mentoring.hadir.add(mentee)
            mentoring.save()
            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:           
            return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            json_input = json.loads(request.body)
            npm = json_input.get("npm")
            kelompok = Kelompok.objects.get(pk=kelompok)
            mentoring = Mentoring.objects.get(kelompok=kelompok, materi=materi)
            mentee = Mentee.objects.get(npm=npm, kelompok=kelompok)
            mentoring.hadir.remove(mentee)
            mentoring.save()
            return HttpResponse(serializers.serialize('json', [mentoring]))
        except Exception as e:           
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def add_pembicara(request, acara):
    # if request.method=='GET':
    #     acara = Acara.objects.get(pk=acara)
    #     return HttpResponse(serializers.serialize('json', [acara.pembicara]))
    if request.method == 'POST':
        try:
            json_input = json.loads(request.body)
            pembicara = Pembicara.objects.get(pk=json_input.get("pembicara"))
            acara = Acara.objects.get(pk=acara)
            acara.pembicara.add(pembicara)
            acara.save()
            return HttpResponse(serializers.serialize('json', [acara]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
   
    elif request.method=='DELETE':
        try:
            json_input = json.loads(request.body)
            pembicara = Pembicara.objects.get(pk=json_input.get("pembicara"))
            acara = Acara.objects.get(pk=acara)
            acara.pembicara.remove(pembicara)
            acara.save()
            return HttpResponse(serializers.serialize('json', [acara]))
        except Exception as e:
                print(str(e))            
                return JsonResponse({"error": str(e)}, status=400)
         
    return JsonResponse({"error": "Method not allowed"}, status=405)
 
@csrf_exempt
def pengurusInti(request):
    if request.method=='GET':
        PI = PengurusInti.objects.all()
        return HttpResponse(serializers.serialize('json', PI))
    if request.method == 'POST':
            try:
                json_input = json.loads(request.body)
                npm=json_input.get("npm")
                if npm is None:
                    raise Exception("NPM tidak boleh kosong")
                elif Mahasiswa.objects.filter(npm=npm).exists():
                    raise Exception("NPM sudah ada")
                nama = json_input.get("nama")
                fakultas = json_input.get("fakultas")
                angkatan = json_input.get("angkatan")
                jurusan = json_input.get("jurusan")
                divisi = DivisiPI(nama=json_input.get("divisi"))
                pengurus_inti = PengurusInti(nama=nama,npm=npm, fakultas=fakultas, angkatan=angkatan, jurusan=jurusan, divisi=divisi)
                pengurus_inti.save()
                return HttpResponse(serializers.serialize('json', [pengurus_inti])) 
            except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405) 
@csrf_exempt
def PI_by_id(request,npm):
    if request.method == 'PUT':
        try:
            pi = PengurusInti.objects.get(pk=npm)
            json_input = json.loads(request.body)
            keys = json_input.keys()
            list_change=[]
            for key in keys:
                if key=="npm":
                    raise Exception("Tidak bisa mengganti NPM")
                elif hasattr(PengurusInti, key):
                    list_change.append(key)  
   
            for attribute in list_change:
                if (attribute=="divisi"):
                    setattr(pi, attribute, DivisiPI.objects.get(nama=json_input.get(attribute)) )
                else:
                    setattr(pi, attribute, json_input.get(attribute))

            pi.save()
            return HttpResponse(serializers.serialize('json', [pi]))
        except Exception as e:            
                return JsonResponse({"error": str(e)}, status=400)
    elif request.method == 'DELETE':
        try:
            PengurusInti.objects.get(pk=npm).delete()
            return HttpResponse(serializers.serialize('json', []))
        except Exception as e:            
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)


def panitia(request):
    if request.method=='GET':
        panitia= Panitia.objects.all()
        return HttpResponse(serializers.serialize('json', panitia))
    return JsonResponse({"error": "Method not allowed"}, status=405)




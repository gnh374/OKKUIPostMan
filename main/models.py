from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255, blank = False)
    fakultas = models.CharField(max_length=255, blank = False)
    angkatan = models.CharField(max_length=255 , blank = False)
    jurusan = models.CharField(max_length=255 , blank = False )
    npm = models.CharField(max_length=255,primary_key= True, blank = False)

    
class Kelompok(models.Model):
    pass

class Mentee(Mahasiswa):
    kelompok = models.ForeignKey(Kelompok, on_delete=models.PROTECT, related_name="mentee" , blank = False)
    jalur_masuk = models.CharField(max_length=255)

class Mentor(Mahasiswa):
    kelompok = models.OneToOneField(Kelompok, on_delete=models.PROTECT,  related_name='mentor' , blank = False)
   
     
class Mentoring(models.Model):
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, related_name = "mentoring" , blank = False)
    waktu = models.DateTimeField( blank = False)
    tempat = models.CharField(max_length = 255, blank = False)
    materi = models.CharField(max_length=255 , blank = False)
    hadir = models.ManyToManyField(Mentee, related_name='mentee_hadir')
    class Meta:
        unique_together = [['kelompok', 'materi']]

class DivisiPI(models.Model):
    nama = models.CharField(max_length=255, primary_key=True , blank = False)
    def __str__(self):
        return self.nama
    
class DivisiBPH(models.Model):
    nama = models.CharField(max_length=255, primary_key=True , blank = False)
    def __str__(self):
        return self.nama
    
class Panitia(Mahasiswa):
    pass
   

class PengurusInti(Panitia):
    divisi =  models.OneToOneField(DivisiPI,  on_delete=models.PROTECT, related_name="pengurusInti" , blank = False)

class BPH(Panitia):

    jabatan = models.CharField(max_length=255, blank = False)
    divisi = models.ForeignKey(DivisiBPH,  on_delete=models.PROTECT, related_name="pengurusBPH" , blank = False)

class Rapat(models.Model):
    divisi = models.ForeignKey(DivisiBPH,  on_delete=models.CASCADE,  related_name="rapat" , blank = False)
    waktu = models.DateTimeField(blank = False)
    tempat = models.CharField(max_length = 255 , blank = False)
    kesimpulan = models.TextField()
    hadir = models.ManyToManyField(BPH, related_name='hadir_rapat')
    class Meta:
        unique_together = [['divisi', 'waktu']]


class Pembicara(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True, blank = False)
    def __str__(self):
        return self.nama
    

class Acara(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True, blank = False)
    tempat = models.CharField(max_length = 255, blank = False)
    waktu_mulai = models.DateTimeField(blank = False)
    waktu_selesai = models.DateTimeField(blank = False)
    pembicara = models.ManyToManyField(Pembicara, related_name="pembicara")
    def __str__(self):
        return self.nama

class Perusahaan(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True, blank = False)

    
class Sponsor(models.Model):
    acara = models.ForeignKey(Acara,  on_delete=models.CASCADE , blank = False)
    perusahaan = models.ForeignKey(Perusahaan,  on_delete=models.CASCADE , blank = False)
    paket = models.CharField(max_length = 25, blank = False)
    class Meta:
        unique_together = [['acara', 'perusahaan']]
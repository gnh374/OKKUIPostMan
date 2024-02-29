from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    fakultas = models.CharField(max_length=255 )
    angkatan = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255 )
    npm = models.CharField(max_length=255, primary_key= True)
    class Meta:
        abstract = True
    
class Kelompok(models.Model):
    pass

class Mentee(Mahasiswa):
    kelompok = models.ForeignKey(Kelompok, on_delete=models.PROTECT, related_name="mentee")
    jalur_masuk = models.CharField(max_length=255)

class Mentor(Mahasiswa):
    kelompok = models.OneToOneField(Kelompok, on_delete=models.PROTECT,  related_name='mentor')
   
     
class Mentoring(models.Model):
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, related_name = "mentoring")
    waktu = models.DateTimeField()
    tempat = models.CharField(max_length = 255)
    materi = models.CharField(max_length=255)
    hadir = models.ManyToManyField(Mentee, related_name='mentee_hadir')
    class Meta:
        unique_together = [['kelompok', 'materi']]

class DivisiPI(models.Model):
    nama = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.nama
    
class DivisiBPH(models.Model):
    nama = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.nama
    
class Panitia(Mahasiswa):
    jenis = models.CharField(max_length=255, default="panitia")
   

class PengurusInti(Panitia):
    divisi =  models.OneToOneField(DivisiPI,  on_delete=models.PROTECT, related_name="pengurusInti")

class BPH(Panitia):
    jabatan = models.CharField(max_length=255)
    divisi = models.ForeignKey(DivisiBPH,  on_delete=models.PROTECT, related_name="pengurusBPH")

class Rapat(models.Model):
    divisi = models.ForeignKey(DivisiBPH,  on_delete=models.CASCADE,  related_name="rapat")
    waktu = models.DateTimeField()
    tempat = models.CharField(max_length = 255)
    kesimpulan = models.TextField()
    hadir = models.ManyToManyField(BPH, related_name='hadir_rapat')


class Pembicara(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True)
    def __str__(self):
        return self.nama
    

class Acara(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True)
    tempat = models.CharField(max_length = 255)
    waktu_mulai = models.DateTimeField()
    waktu_selesai = models.DateTimeField()
    pembicara = models.ManyToManyField(Pembicara, related_name="pembicara")
    def __str__(self):
        return self.nama

class Perusahaan(models.Model):
    nama = models.CharField(max_length = 255, primary_key=True)
    def __str__(self):
        return self.nama
    
class Sponsor(models.Model):
    acara = models.ForeignKey(Acara,  on_delete=models.CASCADE)
    perusahaan = models.ForeignKey(Perusahaan,  on_delete=models.CASCADE)
    paket = models.CharField(max_length = 255)

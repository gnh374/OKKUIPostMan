# OKK UI meets Postman! 
OKK UI meets Postman adalah sebuah platform recreate postman yang digunakan untuk membuat, menguji, dan memelihara API dari OKK UI. Platform ini dapat digunakan untuk melakukan permintaan HTTP ke API OKK UI dengan metode GET, POST, PUT, dan DELETE.

## Instalasi
Clone repository OKKUIPostman dengan menjalankan perintah berikut pada Command Prompt
```bash
git clone https://github.com/gnh374/OKKUIPostMan.git
```

Masuk ke direktori OKKUIPostman lalu buat virtual environment dengan menjalankan perintah berikut
```bash
python -m venv env
```
Aktifkan virtual environment dengan menjalankan perintah berikut
Windows:
```bash
env\Scripts\activate.bat
```
Unix (Mac/Linux):
```bash
source env/bin/activate
```

Instal depedencies dengan menjalankan perintah berikut
```bash
pip install -r requirements.txt
```
Jalankan aplikasi dengan perintah berikut

```bash
python manage.py runserver
```

## Cara Penggunaan

#### POST api/acara/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "nama": "Penutupan OKK UI",
    "tempat": "Balairung",
    "waktu_mulai": "2024-08-01T07:00:00Z",
    "waktu_selesai": "2024-08-01T12:00:00Z",
    "pembicara":[]
}

```

#### GET api/acara/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/acara/
##### param
```bash
Pembukaan OKK UI/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{
    "tempat": "Balai Purnomo",
    "waktu_mulai": "2024-08-01T07:00:00Z",
    "waktu_selesai": "2024-08-01T12:00:00Z",
    "pembicara":[]
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/acara/
##### param
```bash
Acara Puncak OKK UI/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### PUT api/add_pembicara/
##### param
```bash
Pembukaan OKK UI/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{
    "pembicara":"Najwa Shihab"
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/add_pembicara/
##### param
```bash
Pembukaan OKK UI/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{
    "pembicara":"Najwa Shihab"
}
```


#### POST api/sponsor/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "acara":"Pembukaan OKK UI",
    "perusahaan":"RISTEK",
    "paket": "Gold"
}
#pilihan paket hanya Gold, Platinum, dan Silver
```

#### GET api/sponsor/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/sponsor/
##### param
```bash
Pembukaan OKK UI/RISTEK/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{
    "paket": "Platinum"
}
```

#### DELETE api/acara/
##### param
```bash
Pembukaan OKK UI/RISTEK/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```

#### GET api/panitia/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```


#### POST api/pi/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "nama": "Bob Brown",
    "fakultas": "Teknik",
    "angkatan": "2022",
    "jurusan": "Informatika",
    "npm": "1",
    "divisi": "Project Officer (PO)"
}

```

#### GET api/pi/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/pi/
##### param
```bash
1/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{   "fakultas": "Teknik",
    "angkatan": "2023",
    "jurusan": "Informatika",
    "divisi": "Vice Project Officer (VPO)"
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/pi/
##### param
```bash
1/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### POST api/bph/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "nama": "Eve White",
    "fakultas": "Teknik",
    "angkatan": "2022",
    "jurusan": "Informatika",
    "npm": "2",
    "jabatan": "PJ",
    "divisi": "Sponsorship"
}
```

#### GET api/bph/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/bph/
##### param
```bash
2/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{ 
    "fakultas": "Teknik",
    "angkatan": "2023",
    "jurusan": "Informatika",
    "jabatan": "Staff",
    "divisi": "Project"
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/bph/
##### param
```bash
2/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### POST api/rapat/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "divisi": "Sponsorship",
    "waktu": "2024-03-06T10:00:00Z",
    "tempat": "Gedung B",
    "kesimpulan": "Pembahasan anggaran tahun depan",
    "hadir":[]
}

```

#### GET api/rapat/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```
#### POST api/kelompok/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan
```

#### GET api/kelompok/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```


#### POST api/mentor/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "nama": "Jack Smith",
    "fakultas": "Teknik",
    "angkatan": "2022",
    "jurusan": "Informatika",
    "npm": "3",
    "kelompok": "1"
}

```

#### GET api/mentor/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/mentor/
##### param
```bash
3/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{ 
    "fakultas": "Ilmu Komputer",
    "angkatan": "2023",
    "jurusan": "Informatika",
    "kelompok":2
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/mentor/
##### param
```bash
3/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### POST api/mentee/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "nama": "Jane Doe",
    "fakultas": "Teknik",
    "angkatan": "2022",
    "jurusan": "Informatika",
    "npm": "4",
    "kelompok": "1",
    "jalur_masuk": "UTBK"
}


```

#### GET api/mentee/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/mentee/
##### param
```bash
4/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{ 
    "fakultas": "Ilmu Komputer",
    "angkatan": "2023",
    "jurusan": "Informatika",
    "kelompok":2
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/mentee/
##### param
```bash
4/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### POST api/mentoring/
##### param
```bash
#kosongkan
```
##### Body
```bash
{
    "kelompok": "1",
    "waktu": "2024-03-06T08:00:00Z",
    "tempat": "Gedung A",
    "materi": "Pengenalan Python"
}


```

#### GET api/mentoring/
##### param
```bash
#kosongkan
```
##### Body
```bash
#kosongkan 
```

#### PUT api/mentoring/
##### param
```bash
1/Pengenalan Python/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
{
    "waktu": "2024-05-06T08:00:00Z",
    "tempat": "Gedung B"
}
#tidak harus menggunakan semua parameter, gunakan yang ingin diganti saja
```

#### DELETE api/mentoring/
##### param
```bash
1/Pengenalan Python/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```


#### PUT api/hadir-mentoring/
##### param
```bash
1/Pengenalan Python/
```
##### Body
```bash
{
    "npm": "4"
}


```



#### DELETE api/hadir-mentoring/
##### param
```bash
1/Pengenalan Python/

#Jangan lupa menggunakan "/" diakhir nama acara
```

##### Body
```bash
#kosongkan
```




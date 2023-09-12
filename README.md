tautan : https://sectask-nandika.adaptable.app/main/

1.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step !
Pertama, sebelum proyek Django dibuat, saya terlebih dahulu membuat direktori baru dengan nama nandika_inventory. Direktori tersebut saya buat untuk menyimpan data-data tugas 2 saya. 

Selanjutnya saya membuka command prompt dari direktori nandika_inventory untuk mengaktifkan virtual environment. Tujuan dari pengaktifan virtual environment adalah mengisolasi package serta dependencies dari aplikasi sehingga tidak terjadi tabrakan dengan versi lain yang ada pada komputer. Adapun cara pengaktifannya dengan perintah berikut.
env\Scripts\activate.bat

Setelah itu, saya akan menyiapkan dependencies yang tujuannya agar suatu perangkat lunak dapat berfungsi dengan baik termasuk library, framework, atau package. Dependencies yang saya buat saya letakkan pada berkas requirements.txt yang ada di dalam direktori nandika_inventory.

Adapun isi dari dependencies tersebut adalah
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
Setelah isinya dibuat, dependencies tersebut harus dipasang dengan menjalankan perintah di command prompt 
pip install -r requirements.txt

Setelah hal tersebut dilakukan, saya dapat membuat proyek Django baru bernama nandika_project dengan perintah berikut.
django-admin startproject nandika_project .

Setelah membuat proyek Django baru, saya harus menambahkan * pada ALLOWED_HOST di settings.py untuk keperluan deployment yang membuat aplikasi dapat diakses secara luas. Disini ALLOWED_HOST memiliki fungsi sebagai daftar host yang diizinkan untuk dapat mengakses aplikasi web. 

Kemudian, saya harus menjalankan server Django dengan perintah
python manage.py runserver

Setelah itu, saya mengecek ke http://localhost:8000/ untuk mengetahui apakah aplikasi Django yang saya buat sudah berhasil.
Kemudian pada direktori nandika_inventory, saya membuat berkas .gitignore yang digunakan dalam repositori Git untuk menentukan berkas-berkas dan direktori-direkori yang harus diabaikan oleh Git. Berkas ini berfungsi karena pasti ada berkas-berkas yang tidak perlu dilacak oleh Git seperti berkas hasil proses kompilasi, berkas sementara, ataupun berkas konfigurasi pribadi. Adapun isi berkas .gitignore dapat dilihat pada berkas tersebut.

Tahap kedua yang saya lakukan adalah membuat aplikasi main dalam proyek nandika_project dengan perintah berikut.
python manage.py startapp main
Setelah itu, saya harus mendaftarkan aplikasi main ke dalam proyek dengan membuka berkas settings.py di dalam direktori proyek nandika_project. Saya harus menemukan variable INSTALLED_APPS dan menambahkan ‘main’ ke dalam daftar aplikasi yang ada.
Setelah itu saya harus mengatur routing URL agar aplikasi main yang telah saya buat dapat diakes melalui peramban web dengan membuat berkas urls.py di dalam direktori main. Adapun isi dari urls.py diisi dengan kode berikut.
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

Tujuan dari membuat urls.py adalah untuk mengatur rute URL yang terkait dengan aplikasi main. Impor path dan django.urls  digunakan untuk mendefinisikan pola URL. Fungsi show_main dari modul main digunakan sebagai tampilan yang akan ditampilkan saat URL diakses. Variabel app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi.
Selanjutnya, saya akan mengonfigurasi routing URL protek dengan menambahkan rute URL dalam urls,py yang ada di dalam direktori proyek nandika_project. Berkas urls.py pada proyek dibuat untuk bertanggung jawab untuk mengatur rute URL pada tingkat proyek. Pada kode, saya tambahkan
from django.urls import path, include
dengan tujuan untuk mengimpore rute URL dari aplikasi lain ke dalam berkas urls.py.
Saya juga menambahkan rute URL seperti berikut.
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
dengan tujuan untuk mendefinisikan dalam berkasi urls.py aplikasi main. 

Kemudian, saya mengisi berkas models.py untuk mendefinisikan atribut dengan tipe datanya. Adapun isi berkas models.py saya sebagai berikut.
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()

Dari kode tersebut saya mendefinisikan Item sebagai nama model. Lalu name, amount, description, dan price adalah atribut yang saya definisikan juga sesuai dengan instruksi soal.

Setelah itu, saya membuat sebuah fungsi pada views.py yang bertujuan untuk dikembalikan ke dalam sebuah template HTML yang menampilkan aplikasi yang saya buat. Saya mengisi kode berikut pada berkas views.py
from django.shortcuts import render

#Create your views here.
def show_main(request):
    context = {
        'name': 'Tas Sekolah',
        'harga': 'Rp. 50.000',
        'description': 'Tas merupakan jenis ransel yang diproduksi di Indonesia. Tas memiliki banyak varian warna. Terdapat bonus berupa jas hujan sebagai pelindung tas dari hujan ',
        'amount': 25,
    }

    return render(request, "main.html", context)

context adalah dictionary yang berisi data yang akan dikirimkan ke tampilan. return render berguna untuk merender tampilan main.html dengan menggunakan fungsi render. Terdapat 3 argumen dalam fungsi render yaitu request yang berupa objek permintaan HTTP yang dikirim oleh user, main.html yang akan saya buat merupakan nama berkas template yang akan me-render tampilan, dan context berisi dictionary yang berisi data yang akan terus diteruskan ke tampilan sebagai penampilan dinamis.

Setelah itu, saya baru membuat direktori baru bernama templates di dalam direktori aplikasi main. Di dalam direktori templates, saya membuat file baru bernama main.html yang merupakan salah satu argument dalam fungsi render yang saya jelaskan sebelumnya. Adapun inti isi main.html saya sebagai berikut.
<!DOCTYPE html>
<html>
<head>
<style>
</style>
</head>
<body>

<div class="center-text">
  <h1 id="text"><b>Nandika's Inventories</b></h1>
  <h2 id="text">Sedia Perlengkapan Sekolah</h2>
  <h5 id="text">Nama Item : </h5>
  <p id="text">{{ name }}</p>
  <h5 id="text">Harga : </h5>
  <p id="text">{{ harga }}</p>
  <h5 id="text">Jumlah Barang : </h5>
  <p id="text">{{ amount }}</p>
  <h5 id="text">Deskripsi </h5>
  <p id="text">
    {{ description }}
  </p>

</div>
</body>
</html>

Saya juga mengatur color, font, text, dan sebagainya yang dapat dilihat diberkas saya. Sintaks Django {{ name }}, {{ harga }}. {{ amount }}, dan {{ description }} digunakan untuk menampilkan nilai dari variable yang telah didefinisikan dalam context yang ada pada fungsi show_main.
Setelah saya melakukan pengaturan pada views.py, main.html, urls.py dan sebagainya, saya membuat repositori Github baru bernama nandika_inventory dengan visibilitas public. Setelah itu, saya menjalankan migrasi model untuk  melakukan perubahan model yang saya lakukan dengan perintah berikut.
python manage.py makemigrations
python manage.py migrate

Perintah makemigrations menciptakan perubahan model yang belum diaplikasikan ke dalam basis data, sedangkan migrate mengaplikasikan perubahan model yang telah tercantum dalam basis data.
Selain step-step yang diinstruksikan, saya juga membuat unit test dengan membuat berkas tests.py pada direktori aplikasi main. Isi kode test.py dapat dilihat di berkas tests.py. Kode test_main_url_is_exist adalah tes untuk mengecek apakah path URL /main/ dapat diakses, sedangkan kode test_main_using_main_template adalah tes yang digunakan untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.  Lalu, saya menjalankan test dengan perintah
python manage.py test

dan tes berhasil dilakukan.
Kemudian, saya menonaktifkan virtual environment dengan perintah deactivate. Setelah mengaktifkan virtual environment, saya melakukan init, add, commit, push berkas-berkas saya yang ada pada direktori nandika_inventory ke repository nandika_inventory yang ada pada GitHub. Adapun instruksi yang saya berikan saya berikut.
it init
git add . 
git commit -m "commit"
git branch -M main
git remote add origin “link github saya”
git push -u origin main

Agar tampilan saya dapat dilihat oleh orang lain, saya harus melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat. Adapun cara melakukan deployment ke Adaptable adalah sebagai berikut.
1.Pertama, saya harus membuat akun adaptable,io menggunakan akun GitHub
2.Setelah itu login, dan pilih New App. Lalu pilih Connect an Existing Repository.
3.Lalu saya pilih repository nandika_inventory yang isi-isinya merupakan berkas-berkas yang saya push dari direktori saya
4.Kemudian saya memilih branch main
5.Setelah itu, saya memilih Python App Template sebagai template deployment
6.Kemudian saya memilih PostgreSQL sebagai tipe basis data yang akan digunakan
7.Lalu saya menyesuaikan versi python yang ada di komputer saya. Sebelum mengecek saya harus nyalan virtual environment dan jalankan perintah python –version untuk mengetahui versi python saya dan versi python saya 3.10
8.Pada bagian Start Command, saya memasukkan perintah python manage.py migrate&& gunicorn nandika_project.wsgi.
9.Setelah itu saya memberi nama aplikasi sectask-nandika yang akan menjadi domain situs web
10.Kemudian saya mencentang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi
11.Jika proses deployment aplikasi berhasil, saya dapat mengecek tampilan saya melalui 
https://sectask-nandika.adaptable.app/main/

2.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](D:\My Documents\College Task 3\PBP\Bagan.png "Bagan Request CLient ke Web Aplikasi Berbasis Django")


Pada bagan, kita dapat melihat keterkaitan antara urls.py, views.py, dan models.py. urls.py meneruskan request yang diminta client ke views.py, sedangkan views.py mengakses models.py untuk mengambil data-data yang akan diperlukan dan mengakses main.html untuk mengetahui tampilan web. Setelah views.py mengakses models.py dan main.html, views.py akan mengirimkan apa yang telah diakses kepada client melalui url yang direquest oleh client. 

3.Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak terjadi tabrakan dengan versi lain yang ada pada komputer. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment ,tetapi ada kemungkinan mengalami konflik yang disebabkan proyek yang memiliki dependensi yang berbeda. Penggunaan virtual environment sangat disarankan saat mengembangkan aplikasi web berbasis Django atau proyek python lainnya.

4.Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
MVC merupakan singkatan dari Model, View, dan Controller. Model memiliki berfungsi untuk menangani data dan logika bisnis. View berfungsi untuk menampilkan data ke user. Controller bertanggung jawab untuk menerima input dari user dan mengaktifkan model dan view.

MVT adalah singkatan dari Model, View, dan Template. Arsitektur MVT memiliki kemiripan dengan MVC. Akan tetapi, MVT tidak memiliki controller. Fungsi controller pada MVT diimplementasikan oleh template. Template diimplementasikan sebagai file HTML yang berisi kode python untuk melakukan aktivasi model dan view.

MVVM adalah singkatan dari Model-View-ViewModel. MVVM merupakan gabungan dari MVC dan MVT. Pada awalnya, arsitektur MVVM digunakan di dalam Windows Presentation Foundation dan Silverlight. Pada arsitektur MVVM, view tidak bertanggung jawab untuk menampilkan data ke user. View bertanggung jawab untuk menampilkan data yang disediakan oleh ViewModel.

Beberapa perbedaan antara arsitektur MVC, MVT, dan MVVM adalah :
.> Pada arsitektur MVC memiliki controller, sedangkan Arsitektur MVT dan MVVM tidak memiliki controller.
.> Pada arsitektur MVC, view dapat mengakses model secara langsung, sedangkan arsitektur MVVM, view mengakses data melalui ViewModel. 
.> Pada arsitektur MVC dan MVT tidak memiliki ViewModel, sedangkan MVVM memiliki VidewModel.
.> Pada arsitektur MVVM memiliki konsep binding dua arah, di mana perubahan pada view akan memengaruhi ViewModel dan sebaliknya. Sedangkan .arsitektur MVC dan MVT tidak.
.> Pada arsitektur MVT, template digunakan untuk mengatur tampilan halaman web, sedangkan pada arsitektur MVC dan MVVM, view yang mengatur tampilan aplikasi.

Referensi :
Musyaffa, I. 2023. MVC vs MVP vs MVVM : Apa Perbedaannya & Mana yang terbaik diantara ketiganya?. agus-hermanto.com. Diakses dari
 https://agus-hermanto.com/blog/detail/mvc-vs-mvp-vs-mvvm-apa-perbedaannya-mana-yang-terbaik-diantara-ketiganya-a



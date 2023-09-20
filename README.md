Nandika Rafi Atallah
PBP C
2206082745
Tugas 2
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

![Bagan](Bagan.png "Bagan Model, View, Template")

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


Tugas 3
1. Apa perbedaan antara form POST dan form GET dalam Django?

Terdapat beberapa perbedaan antara form POST dan form GET dalam Django adalah sebagai berikut.
Yang pertama adalah metode pengirim data. Pada form POST, data dikirim ke server sebagai bagian dari permintaan HTTP, sedangkan pada form GET, data dikirim sebagai bagian dari URL dalam string query. 
Yang kedua adalah tampilan data. Pada form POST, data tidak terlihat pada URL yang membuat data lebih aman, sedangkan pada form GET, data terlihat pada URL yang membuat data sensitif tidak cocok untuk menggunakan form GET.
Yang ketiga adalah caching. Pada form POST, data yang dikirim tidak akan di-cache oleh browser atau server proxy, sedangkan pada form GET, data yang dikirim dapat di-cache oleh browser atau server proxy karena data tersebut ada pada URL.
Yang keempat adalah idempotensi.Idempotensi berarti melakukan permintaan yang sama beberapa kali tidak mengubah keadaan server. Pada form POST, permintaan POST tidak dianggap Idempoten yang berarti akan mengubah keadaan server. Hal ini dikarenakan form POST digunakan untuk membuat atau memperbarui entitas, sedangkan pada form GET, permintaan dianggap sebagai Idempoten yang berarti tidak mengubah keadaan server. Form GET seharusnya hanya digunakan untuk membaca data bukan untuk membuat atau memperbaruinya.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengirim data terletak pada tujuannya. Tujuan dari XML adalah pertukaran data antara sistem dan platform yang berbeda sehingga struktur datanya sangat kompleks, tetapi masih tetap bisa dibaca. XML memiliki markup yang lebih lengkap daripada JSON. Tujuan dari JSON adalah pertukaran data antara aplikasi web dan server. Struktur data dan kode yang digunakan dalam JSON tidak begitu kompleks dan sangat mudah untuk dimengerti. JSON lebih fokus pada struktur data berbeda dengan XML yang lebih fokus pada markup. Tujuan dari HTML adalah untuk membuat tampilan halaman web dan menyusun konten yang dapat dilihat oleh pengguna di browser web. HTML bukan format data yang dirancang untuk pertukaran data, tetapi lebih sebagai bahasa untuk menyampaikan informasi. 

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena stuktur datanya ringan yang semi terstruktur sehingga memiliki fleksibelitas yang tinggi dalam melakukan proses transfer data. JSON memiliki kompatibilitas dengan berbagai bahasa pemrograman baik itu JavaScript, Java, Python, C++, dan sebagainya.  Selain itu, JSON mudah diintegrasikan dengan berbagai sistem baik perangkat web, perangkat seluler, perangkat IoT (Internet of Things), serta layanan cloud seperti SaaS (Software as a Service) dan PaaS (Platform as a Service).

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

Saya akan menjelaskan bagaimana cara saya mengimplementasikan checklist tersebut secara step by step dengan penjelasan sebagai berikut.
Pertama, sebelum membuat input form untuk menambahkan objek model, saya harus mengubah kode yang ada pada urls.py pada folder nandika_project. Adapun sebelum mengubah kode, seperti biasa, saya harus mengaktifkan virtual environment saya dengan menjalankan perintah env\Scripts\activate.bat pada terminal.Setelah itu, saya harus mengubah path ‘main/’ menjadi ‘’ yang ada pada list urlpatterns sehingga saya dapat mengakses http://localhost:8000/ yang sebelumnya http://localhost:8000/main saat menjalankan python manage.py runserver di terminal. 

Setelah itu, saya harus mengimplementasi skeleton sebagai kerangka views dari situs web yang saya buat. Tujuan dibuatnya kerangka views ini adalah untuk memastikan adanya konsistensi dalam desain situs web kita serta memperkecil kemungkinan terjadinya redudansi kode. Kemudian saya membuat folder baru pada root folder nandika_inventory bernama templates. Di dalam folder ini, saya akan menyimpan file yang bernama base.html yang isinya dapat dilihat pada file saya tersebut. Tujuan dari file base.html yang saya buat adalah sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek saya. Setelah membuat file base.html, saya memperbarui file settings.py yang ada pada nandika_project dan menambah sesuatu yang ada pada variable TEMPLATES. Saya mengubah isi ‘DIRS’ menjadi  'DIRS': [BASE_DIR / 'templates']. Setelah itu saya menambahkan {% extends 'base.html' %} pada file main.html yang berada pada folder templates dengan tujuan menjadikan base.html sebagai template utama. 

Setelah itu, saya baru dapat membuat form input Data. Saya harus membuat file yaitu forms.py pada folder main. Lalu untuk isinya dapat dilihat pada file saya. Model untuk menunjukkan model yang digunakan untuk form. Ketika form disimpan, form akan disimpan pada objek Item yang telah saya definisikan pada models.py. Fields adalah field dari model Item yang digunakan untuk form.  Kemudian, pada file views.py saya menambahkan beberapa import pada bagian atas yaitu from django.http import HttpResponseRedirect , from main.forms import ProductForm, dan from django.urls import reverse. Setelah itu, saya menambahkan fungsi baru pada file views.py yaitu create_product yang dapat dilihat pada file saya tersebut. form = ProductForm(request.POST or None) digunakan untuk membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada request.POST. Adapun form.is_valid() digunakan untuk memvalidasi input. form.save() digunakan untuk menyimpan data dari form tersebut dan return HttpResponseRedirect(reverse('main:show_main')) digunakan untuk melakukan redirect data pada form berhasil disimpan. Setelah itu, saya menambahkan beberapa hal pada fungsi show_main yang ada di views.py. Saya menambahkan products = Item.objects.all() untuk mengambil seluruh object Product yang tersimpan pada database. Di dalam context saya juga menambahkan ‘products’ : products . Setelah itu, saya menambahkan import pada urls.py yang ada pada folder main yaitu impor fungsi create_product sehingga instruksi impornya menjadi  from main.views import show_main, create_product. Setelah itu, saya menambahkan path url ke dalam urlpatterns yang ada pada file urls.py di folder main agar program dapat mengakses fungsi yang sudah di-import sebelumnya dengan menambahkan path('create-product', create_product, name='create_product'),. Setelah itu, saya membuat HTML baru dengan nama create_product.html pada direktori main/templates. Kodenya dapat dilihat pada file saya tersebut. Dalam penjelasannya, <form method=”POST”> berfungsi untuk menandakan block untuk form dengan metode POST. {% csrf_token %} adalah token security yang akan di-generate secara otomatis oleh Django untuk mencegah serangan yang membahayakan. {{ form.as_table }} berfungsi untuk menampilkan fields form yang sudah dibuat pada form sebagai table. Bagian <input type="submit" value="Add Product"/> fungsinya untuk tombol submit dan mengirimkan request ke view.  Setelah itu, saya menambahkan beberapa hal pada main.html saya yaitu button dan tabel input saya yang kodenya dapat dilihat di file saya. Kemudian, saya dapat menjalankan python manage.py runserver dan membuka http://localhost:8000 untuk melihat apakah berhasil atau tidak.

Selanjutnya, saya akan mengembalikan data dalam bentuk XML. Saya akan menambahkan from django.http import HttpResponse dan from django.core import serializers ke file views.py yang ada di folder main. Kemudian, pada file tersebut saya menambahkan fungsi def show_xml(request) yang isinya adalah data = Item.objects.all() . Setelah itu, saya menambahkan return function berupa HttpResponse dengan kode berikut return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") . Pada kode tersebut, import serializers digunakan untuk mentranslasi objek model menjadi format lain seperti XML. Selanjutnya, saya membuka urls.py yang berada di folder main dan menambahkan impor fungsi show_xml. Saya juga menambahkan path('xml/', show_xml, name='show_xml'), pada urlpatterns yang terletak di file urls.py yang ada di folder main. Setelah itu, saya dapat menjalankan python manage.py runserver di terminal dan membuka http://localhost:8000/xml untuk melihat tampilan XML saya. 

Selanjutnya, saya akan mengembalikan data dalam bentuk JSON. Dengan cara yang sama seperti sebelumnya, saya membuka file views,py yang ada pada folder main dan menambahkan fungsi show_json dengan parameter request yang isi kodenya adalah data = Item.objects.all() . Lalu dibawahnya, saya menambahkan return function yaitu  return HttpResponse(serializers.serialize("json", data), content_type="application/json") yang berisi data hasil query yang sudah diserialisasi menjadi JSON. Setelah itu, saya menambah import show_json pada file urls.py yang ada di folder main agar dapat mendapat akses fungsi tersebut. Setelah itu, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi dengan kode path('json/', show_json, name='show_json'), . Setelah itu, saya menjalankan runserver python lagi dan membuka http://localhost:8000/json untuk mengecek tampilan JSON. 

Selanjutnya, saya akan mengembalikan data berdasarkan ID baik dalam bentuk XML ataupun JSON. Pertama, saya membuka views.py yang ada pada folder main dan buat sebuah fungsi dengan parameter request yaitu show_xml_by_id untuk XML dan show_json_by_id untuk JSON. Setelah itu di dalam setiap fungsi, tambahkan data = Item.objects.filter(pk=id). Dibawahnya, saya menambahkan kode return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") untuk XML dan return HttpResponse(serializers.serialize("json", data), content_type="application/json") untuk JSON. Kemudian, tambahkan import show_xml_by_id dan show_json_by_id pada file urls.py yang ada pada folder main. Kemudian, saya menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi yaitu path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id') dan path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),. Setelah itu, saya menjalankan perintah python manage.py runserver dan membuka http://localhost:8000/xml/[id] dan http://localhost:8000/xml/[id] . id berisi sebuah bilangan 1,2,3,..n dan seterusnya sesuai dengan berapa n data yang saya input. 

Setelah berhasil melakukan step-step tersebut, saya tidak lupa untuk melakukan add, commit, dan push ke repository github dan juga mematikan virtual environment.

5. Adapun kelima URL berhasil saya akses di Postman dan saya akan melampirkan dokumentasinya
Berikut adalah screenshoot dari hasil akses URL pada Postman
A. HTML
![html](Screenshoot_HTML.png "Views HTML")

B. XML
![xml](Screenshoot_XML.png "Views XML")

C. JSON
![json](Screenshoot_JSON.png "Views JSON")

D. XML by ID
![xml by id](Screenshoot_XML_id.png "Views XML by ID")

E. JSON by ID
![json by id](Screenshoot_JSON_id.png "Views JSON by ID")


Referensi :
- Patria, R. 2021. Yuk Kenalan Dengan JSON: Fungsi & Struktur Dalam Pemrograman. domainesia.com. Diakses dari
https://www.domainesia.com/berita/json/
- Setiawan, R. 2021. Apa itu JSON? Simak Perbedaannya dengan XML : Apa Perbedaannya & Mana yang terbaik diantara ketiganya?. dicoding.com. Diakses dari
https://www.dicoding.com/blog/apa-itu-json/
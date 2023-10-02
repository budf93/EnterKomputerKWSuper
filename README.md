Nama            : Fikri Budianto
Kelas           : PBP F
Link Adaptable  : https://enterkomputerkwsuper.adaptable.app/main/

Checklist untuk tugas ini adalah sebagai berikut:

 Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut

 Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
 Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    Manfaat dari penggunaan element selector di dalam CSS adalah kita bisa membuat tampilan elemen HTML yang konsisten, mudah untuk diimplementasikan, efisien untuk digunakan, mudah untuk dimaintain, mempercepat pengembangan, dan lebih mudah untuk dimanage. Kita dapat menggunakan element selector ketika kita ingin mengubah style dari elemen-elemen HTML yang bersifat default, ketika kita ingin membuat design yang konsisten, untuk mereset styling yang sudah ada, ketika kita ingin memmbuat fondasi dasar untuk styling dari elemen, dan untuk mengubah styling elemen HTML secara cepat.
 2. Jelaskan HTML5 Tag yang kamu ketahui.
   - <head> : berisi metadata mengenai website 
   - <!--...--> : digunakan untuk comment pada kode HTML
   - <li> : menandakan suatu item dari suatu daftar
   - <ol> : menandakan suatu ordered list/daftar terurut
   - <ul> : menandakan suatu unordered list/daftar tidak terurut
   - <p> : menandakan suatu paragraf di dalam tampilan website
   - <img> : menandakan suatu objek gambar
   - <h1> to <h6> : menandakan suatu header di dalam tampilan website
   - <button> : menandakan suatu tombol di dalam suatu website, bisa merujuk ke suatu website
   - <strong> : untuk menebalkan suatu bagian dari suatu teks
   3. Jelaskan perbedaan antara margin dan padding.
    Margin merupakan ruang yang terdapat di luar suatu elemen. Margin tidak memiliki warna background dan tidak memengaruhi warna background dari suatu elemen. Selain itu, margin juga menciptakan jarak antara suatu elemen dengan elemen lain.
    Padding merupakan jarak yang terdapat diantara konten dan border dari suatu elemen. Padding memiliki warna background dan memengaruhi warna background dari suatu elemen. Selain itu, padding tidak memengaruhi spacing antar elemen.
 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    Bootstrap merupakan framework yang sudah lama dikembangkan dan banyak dipakai karena sifatnya yang responsif dan efisien. Bootstrap menyediakan komponen-komponen untuk membuat UI yang sudah dibuat sebelumnya sehingga memudahkan pekerjaan programmer. Selain itu, Bootstrap juga memiliki ukuran berkas yang besar. Akan tetapi, Bootstrap sulit untuk dikostumisasi karena Bootstrap memiliki banyak sekali komponen pembangun yang sudah baku.
    Di sisi lain, CSS Tailwind merupakan framework yang tergolong baru dan masih terus dikembangkan menjadi lebih baik lagi. CSS Tailwind merupakan utility-first framework yang memberikan fleksibilitas kepada programmer untuk mengkostumisasikan tampilan website. Hal ini berbanding terbalik dengan Bootstrap yang cenderung lebih sulit untuk dikostumisasi. CSS Tailwind juga memiliki ukuran berkaas yang lebih kecil bila dibandingkan dengan Bootstrap.
    CSS Tailwind lebih baik digunakan apabila kita memerlukan kostumisasi yang lebih leluasa pada website yang kita punya sedangkan Bootstrap lebih baik apabila kita ingin membuat aplikasi web dan mobile yang lebih responsif.
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Pertama-tama saya menambahkan dulu Bootstrap ke dalam aplikasi dengan cara menambahkan kode-kode berikut ke templates/base.html.
   <head>
      {% block meta %}
         <meta charset="UTF-8" />
         <meta name="viewport" content="width=device-width, initial-scale=1">
      {% endblock meta %}
   </head>   
   Kode berikut bertujuan agar halaman web yang saya punya dapat menyesuaikan ukuran dari perilaku perangkat mobile.
   Lalu, saya menambahkan Bootstrap CSS dan juga JS. Hal itu dicapai dengan menambahkan kode berikut ke dalam base.html:
   <head>
   ...
      {% block meta %}
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
      {% endblock meta %}
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
      <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
   </head>
   Lalu, saya membuat navbar dengan cara menambahkan kode berikut sebelum bagian body:
   <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="https://sidang.cs.ui.ac.id/static/media/fasilkom.5f08cf824cb2e94af912.png" alt="Logo" width="30" height="30" class="d-inline-block align-text-top">
                Fikri Budianto
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{% url 'main:logout' %}">Tombol Logout</a>
                    </li>
                </ul>
                <span class="navbar-text">
                Toko Komputer Terpercaya Anda   
                </span>
            </div>
        </div>
    </nav>
    Kode diatas bertujuan untuk menampilkan navbar yang berisi nama saya, tombol logout, dan slogan yang bebas untuk diisi apapun. Navbar ini nantinya juga akan menampilkan logo Fasilkom UI di bagian pojok kiri.

    Lalu, saya membuat fitur edit dengan cara pertama-tama membuat fungsi baru yang bernama edit_product yang menerima parameter    request dan id. Fungsi yang dibuat adalah sebagai berikut:

    def edit_product(request, id):
    # Get product berdasarkan ID
      product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
      form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
      # Simpan form dan kembali ke halaman awal
      form.save()
      return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

    Lalu, saya membuat berkas HTML baru yang bernama edit_product.html pada subdirektori main/templates. Berkas tersebut saya isi dengan kode berikut:

      {% extends 'base.html' %}

      {% load static %}

      {% block content %}

      <h1>Edit Product</h1>

      <form method="POST">
         {% csrf_token %}
         <table>
            {{ form.as_table }}
            <tr>
                  <td></td>
                  <td>
                     <input type="submit" value="Edit Product"/>
                  </td>
            </tr>
         </table>
      </form>

      {% endblock %}

      Lalu, pada berkas urls.py saya mengimport fungsi edit_product dan menambahkan path url ke dalam urlpatterns dengan cara menambahkan kode berikut : 

      from main.views import edit_product.
      
      Lalu, saya menambahkan kode berikut untuk menambahkan path url ke dalam urlpatterns:

      ...
      path('edit-product/<int:id>', edit_product, name='edit_product'),
      ...

      Lalu, saya menmabahkan kode berikut ke dalam main.html yang berada di main/templates agar terlihat tombol edit pada setiap baris tabel:
      ...
      <tr>
         ...
         <td>
            <a href="{% url 'main:edit_product' product.pk %}">
                  <button>
                     Edit
                  </button>
            </a>
         </td>
      </tr>
      ...

      Setelah saya saya menambahkan fitur edit, saya membuat fungsi untuk menghapus produk. Pertama-tama, saya membuat fungsi delete_product dengan kode sebagai berikut :

      def delete_product(request, id):
         # Get data berdasarkan ID
         product = Product.objects.get(pk = id)
         # Hapus data
         product.delete()
         # Kembali ke halaman awal
         return HttpResponseRedirect(reverse('main:show_main'))

      Lalu, di dalam file urls.py saya mengimport fungsi tersebut dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor dengan cara menambahkan kode berikut :

      from main.views import delete_product

      Lalu kode berikut:

      ...
      path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
      ...  

      Setelah itu, saya menambahkan kode berikut pada main.html pada folder main/templates agar terdapat tombol hapus untuk setiap produk.

      ...
      <tr>
         ...
         <td>
            <a href="{% url 'main:edit_product' product.pk %}">
                  <button>
                     Edit
                  </button>
            </a>
            <a href="{% url 'main:delete_product' product.pk %}">
                  <button>
                        Delete
                  </button>
               </a>
         </td>
      </tr>
      ...

   

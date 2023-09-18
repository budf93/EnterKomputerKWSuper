Nama            : Fikri Budianto
Kelas           : PBP F
Link Adaptable  : https://enterkomputerkwsuper.adaptable.app/main/

1. Apa perbedaan antara form POST dan form GET dalam Django?
- Pada form GET, suatu data diminta dari resource tertentu, sedangkan pada form POST data dikirim untuk diproses pada resource tertentu.
- GET hanya boleh digunakan untuk memproses permintaan yang tidak memengaruhi kondisi dari sistem, sedangkan POST memang ditujukan untuk digunakan untuk memproses permintaan yanng dapat mengubah kondisi sistem.
- GET menambahkan from-data ke dalam URL dalam bentuk pasangan name-value, sedangkan POST menambahkan from-data ke dalam body dari permintaan permintaan HTTP sehingga data tidak ditampilkan di dalam URL.
- GET tidak dapat digunakan untuk mengirimkan data binary seperti gambar atau dokumen, sedangkan POST dapat digunakan untuk mengirimkan data ASCII dan juga data binary.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Perbedaan antara XML, JSON, dan HTML adalah XML dan JSON digunakan untuk penyimpanan dan pengiriman data, sedangkan HTML digunakan untuk mendeskripsikan bagaimana data tersebut ditampilkan di layar. Selain itu, walaupun XML dan JSON memiliki kemiripan dari segi penggunaan, terdapat beberapa perbedaan juga antara XML dan JSON.

JSON memiliki fitur array yang dapat digunakan untuk menyimpan objek, tidak menggunakan end tag, dan lebih mudah untuk dibaca dan ditulis dibandingkan XML. Namun, dari segi keamanan XML memiliki tingkat keamanan yang lebih tinggi dibandingkan JSON. XML juga memiliki fitur komentar dan XML memiliki dukungan untuk berbagai macam jenis encoding, berlawanan dengan JSON yang hanya mendukung encoding UTF-8

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena:
- Ukuran file dari JSON yang sangat ringan
- Sifat dari berkas JSON yang mudah dibaca dan dipahami oleh programmer lain
- Hampir semua bahasa pemrograman yang populer memiliki kemampuan untuk membaca file JSON dan mengkonversikannya menjadi suatu objek atau class

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Melakukan add-commit-push ke GitHub.

Checklist untuk tugas ini adalah sebagai berikut:

Sebelum saya membuat form registrasi, pertama-tama saya mengatur routing dari main/ ke / lalu membuat skeleton sebagai kerangka views untuk memastikan adanya konsistensi dalam desain kode saya sehingga mengurangi adanya redundansi kode.

Setelah saya membuat skeleton sebagai kerangka views, saya mulai mengerjakan checklist masing-masing. Penjelasan mengenai pengerjaan langkah demi langkah dari setiap checklist adalah sebagai berikut:
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
    
Untuk membuat sebuah input form, pertama-tama saya membuat berkas baru pada direktori main yang bernama forms.py untuk membuat struktur form yang dapat menerima data produk baru. Saya menambahkan kode berikut ke dalam forms.py:

from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "price", "description"]

model = Product menunjukkan bahwa ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah object Product dengan field dari model Product yaitu name, amount, price, dan description.

Lalu, saya membuat fungsi baru yang bernama create_product yang menerima parameter request untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form. Kode dari create_product adalah sebagai berikut:

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

Lalu, saya mengubah fungsi show_main pada berkasi views.py menjadi sebagai berikut:

def show_main(request):
    products = Product.objects.all() ->  untuk mengambil seluruh object Product yang tersimpan pada database.

    context = {
        'name': 'Fikri Budianto', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'nama_toko': "EnterKomputerKWSuper",
        'products': products
    }

    return render(request, "main.html", context)

Setelah itu, pada berkas urls.py pada main saya mengimport fungsi create_product lalu menambahkan path url ke dalam urlpatterns pada urls.py pada main untuk mengakses fungsi create_product yang baru saja diimport.

Lalu, saya membuat berkas HTML baru dengan nama create_product.html pada direktori main/templates yang saya isi dengan kode berikut:

    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}   

Setelah itu, saya menambahkan kode berikut pada main.html untuk menampilkan data produk dalam bentuk tabel serta tombol "Add New Product" yang akan redirect ke halaman form. 

    ...
    <table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_pr oduct' %}">
        <button>
            Add New Product
        </button>
    </a>

    {% endblock content %}

2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
    Untuk membuat fungsi views yang melihat objek yang sudah ditambahkan dalam format HTML, pertama-tama saya menambahkan kode berikut:

    def show_main(request):
        products = Product.objects.all()

        context = {
            'name': 'Fikri Budianto', # Nama kamu
            'class': 'PBP F', # Kelas PBP kamu
            'nama_toko': "EnterKomputerKWSuper",
            'products': products
        }

        return render(request, "main.html", context)

    Fungsi ini bertujuan untuk melihat objek yang sudah ditambahkan dalam format HTML.

    Lalu, saya menambahkan fungsi ini yang bertujuan untuk mengembalikan data dalam bentuk XML.

    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")   

    Lalu, saya menambahkan fungsi ini untuk mengembalikan data dalam bentuk JSON.

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")     
    
    Fungsi-fungsi diatas mengembalikan object HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json"

    Setelah itu, saya menambahkan kedua fungsi ini yang masing-masing bertujuan untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON. Fungsi-fungsi ini menerima parameter request dan id dan mengembalikan HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON). Variabel data = Product.objects.filter(pk=id) menyimpan hasil query dari data dengan id tertentu yang ada pada Product.

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

    Setelah saya menambahkan fungsi-fungsi di atas pada views.py, saya membuat rounting URL untuk masing-masing views yang telah ditambahkan untuk mengakses fungsi-fungsi yang telah dibuat. 

    Hal tersebut saya lakukan dengan pertama-tama mengimpor semua fungsi yang diperlukan dari main.views dengan cara sebagai berikut:

    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

    Lalu, saya tambahkan path url berikut ke dalam urlpatterns pada urls.py untuk mengakses yang baru saja diimpor.

    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),



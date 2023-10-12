Nama            : Fikri Budianto
Kelas           : PBP F
Link Adaptable  : https://enterkomputerkwsuper.adaptable.app/main/

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming adalah suatu arsitektur yang bersifat non-blocking dimana arsitektur ini tidak menghalangi eksekusi operasi ketika terdapat satu atau lebih operasi yang sedang berjalan karena asnychronous programming bersifat multithreading yang membolehkan beberapa operasi untuk berjalan pada saat yang sama. Dengan menggunakan asynchronous programming, beberapa operasi yang terkait dapat berjalan pada saat yang bersamaan menurunkan lag time dan mempercepat waktu eksekusi operasi-operasi yang sedang berjalan. Kekurangan dari asynchronous programming adalah kode-kode yang menggunakan asynchronous programming lebih kompleks dan lebih sulit untuk dibaca.

Synchronous programming adalah suatu arsitektur yang bersifat blocking sehingga eksekusi operasi haruslah berjalan secara berurutan atau sekuensial. Synchronous programming bersifat single-thread sehingga hanya satu request pada suatu waktu yang akan dikirim ke server dan operasi akan menunggu hingga request tersebut dijalankan oleh server. Kelebihan dari synchronous programming adalah penulisan dari kode menjadi lebih mudah dan pembacaan kode menjadi lebih mudah juga.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan sebuah paradigma dimana jalannya program ditentukan oleh tindakan-tindakan dari luar programn seperti pengguna yang memasukkan input dari keyboard atau sensor yang menerima data dari luar. Salah satu penerapan paradigma event-driven programming pada tugas ini adalah penerapan AJAX yang memungkinkan halaman web untuk memperbarui data secara asinkronus dengan mengirimkan data ke peladen di balik layar. Hal tersebut berarti bahwa kita dapat memperbarui sebagian elemen data pada halaman tanpa harus mereload halaman secara keseluruhan.

3. Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX diimplementasikan dengan cara script mengirimkan request ke server dan melanjutkan eksekusi tanpa harus menunggu reply dari server. Ketika terdapat reply dari server maka suatu browser event akan terjadi yang nantinya akan membuat script menjalankan suatu tindakan tertentu sesuai reply yang diterima. 

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API merupakan API yang native di dalam JavaScript sehingga kita tidak perlu menambahkan library tambahan untuk menggunakan Fetch API, sedangkan jQuery merupakan library eksternal yang perlu ditambahkan sebelum digunakan.

FetchAPI memiliki performa yang lebih baik karena bersifat native dan memiliki ukuran yang lebih kecil dibandingkan jQuery, sedangkan jQuery merupakan library yang lebih besar dibandingkan FetchAPI dan memiliki fungsionalitas yang lebih lengkap.

FetchAPI didukung oleh sebagian besar browser jaman sekarang. Namun, di beberapa browser lama FetchAPI tidak tersedia, sedangkan jQuery didukung oleh berbagai macam browser termasuk browser yang sudah lama.

Fetch API lebih baik digunakan apabila:
- Kita ingin membuat aplikasi web untuk browser yang lebih baru
- Kita ingin membuat solusi yang lebih ringan ketika membuat request AJAX

jQuery lebih baik digunakan apabila:
- Kita ingin memberikan dukungan bagi browser lama yang tidak mendukugn Fetch API
- Kita sudah menggunakan jQuery untuk melaksanakan tugas lain di dalam projek kita
- Kita ingin menggunakan API yang lebih ringkas dan konsisten untuk beragam manipulasi DOM dan membuat request AJAX 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk melakukan pengambilan task menggunakan AJAX GET, pertama-tama saya membuat fungsi get_product_json di views.py untuk mengambil semua produk. Fungsi yang saya tambahkan adalah sebagai berikut: 

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item)) 

Lalu, saya menambahkan fungsi add_product_ajax. Kode yang saya tambahkan adalah sebagai berikut:

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

Lalu, di urls.py saya mengimpor fungsi get_product_json dan lalu Menambahkan Routing Untuk Fungsi get_product_json dan add_product_ajax dengan menambahkan kode berikut pada urlpatterns: 

...
path('get-product/', get_product_json, name='get_product_json'),
path('create-product-ajax/', add_product_ajax, name='add_product_ajax')

Kemudian, saya menambahkan script yang berisi fungsi getProducts() dan refreshProducts() agar pengguna tidak perlu merefresh pagenya setiap kali ada perubahan. Kode yang saya tembahkan adalah sebagai berikut: 

<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }

    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()
</script>

Lalu, saya membuat modal sebagai form untuk menambahkan produk. Kode yang saya tambahkan adalah sebagai berikut:

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>

Lalu, saya menambahkan button yang berfungsi untuk menampilkan model:

<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>

Lalu, saya membuat fungsi baru pada block script yang bertujuan untuk menambahkan data berdasarkan input ke basis data secara AJAX dengan fungsi yang saya tulis adalah sebagai berikut :

function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}

Lalu, saya menambahkan fungsi onclick pada button "Add Product" pada modal untuk menjalankan fungsi addProduct() dengan menambahkan kode berikut.

<script>
    ...
    document.getElementById("button_add").onclick = addProduct
</script>

Terakhir, saya menjalankan collectstatic setelah menulis kode yang diperlukan:

python manage.py collectstatic

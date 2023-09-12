from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fikri Budianto',
        'class': 'PBP F',
        'nama_toko': "EnterKomputerKWSuper"
    }

    return render(request, "main.html", context)

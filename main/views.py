from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Tas Sekolah',
        'harga': 'Rp. 50.000',
        'description': 'Tas merupakan jenis ransel yang diproduksi di Indonesia\nTas memiliki banyak varian warna\nTerdapat bonus berupa jas hujan sebagai pelindung tas dari hujan ',
        'amount': 25,
    }

    return render(request, "main.html", context)
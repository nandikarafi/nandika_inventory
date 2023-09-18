from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'name': 'Nandika Rafi Atallah',
        'kelas': 'PBP C',
    }

    return render(request, "main.html", context)
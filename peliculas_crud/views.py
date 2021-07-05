from django.shortcuts import render

def indexView(request):
    return render(request, 'peliculas_crud/index.html')

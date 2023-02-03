from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import Cafe, GeeksModel
from .forms import CafeForm, GeeksForm
from django.core import serializers
from django.http import JsonResponse, HttpResponseBadRequest
import json

# Create your views here.


# Create your views here.
def index(request):  # <<==========
    return render(request, "index_master.html")  # <<==========


def home(request):
    return render(request, "menu.html")


def pruebas(request):
    return render(request, "contenido.html")


def cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'productos/homecafe.html', {
        'cafes': cafes,
    })


# def agregar(request):
#     if request.method == "POST":
#         form = CafeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homecafe')
#     else:
#         form = CafeForm()
#     context = {'form': form}
#     return render(request, 'productos/agregarcafe.html', context)


def agregar(request):
    if request.method == "POST":
        print("entro")
        form = CafeForm(request.POST)
        if form.is_valid():
            print("es valido")
            form.save()
            return HttpResponse()
        else:
            print("No es valido")
            return JsonResponse({"error": form.errors}, status=400)
    else:
        print("no es post")


# *********************************************************************************


# def eliminar(request, cafe_id):
#     cafecito = Cafe.objects.get(codCafe=cafe_id)
#     cafecito.delete()
#     return redirect('homecafe')

def eliminar(request):
    cafe_id = request.POST.get('codCafe')
    cafecito = get_object_or_404(Cafe, codCafe=cafe_id)
    cafecito.delete()
    return HttpResponse()


def editar(request, cafe_id):
    cafecito = Cafe.objects.get(codCafe=cafe_id)
    if request.method == "POST":
        form = CafeForm(request.POST, instance=cafecito)
        if form.is_valid():
            form.save()
            return redirect('homecafe')
    else:
        form = CafeForm(instance=cafecito)

    context = {'form': form,
               'cafecito': cafecito}
    return render(request, 'productos/editarcafe.html', context)

# def editar(request):
#     cafes = Cafe.objects.values()
#     Cafe_id = request.POST.get('codCafe')

#     formx = cafes.get(codCafe=Cafe_id)
#     print(formx)
#     return JsonResponse(formx)


def ejemplos(request):
    return render(request, 'productos/ejemplos.html')


def ddavimo(request):
    return render(request, 'layouts/layouts_principal.html')


def ventas(request):
    return render(request, 'Ventas/index.html')


# Geeks
def index(request):
    return render(request, 'geeks/index.html')


def create_view(request):
    context = {}
    form = GeeksForm(request.POST)
    if form.is_valid():
        form.save()
        context["prueba"] = GeeksModel.objects.all()
        return render(request, "geeks/list_view.html", context)
    context['form'] = form
    return render(request, 'geeks/create_view.html', context)


def list_view(request):
    context = {}
    context["prueba"] = GeeksModel.objects.all()
    return render(request, "geeks/list_view.html", context)


def detail_view(request, id):
    context = {}
    print(id)
    context["data"] = GeeksModel.objects.get(id=id)
    return render(request, "geeks/detail_view.html", context)


def update_view(request):
    context = {}
    if request.method == 'POST':
        lid = request.POST['lid']
        obj = get_object_or_404(GeeksModel, id=lid)
        form = GeeksForm(request.POST, instance=obj)
        print(form)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("geeks/list.html")
    else:
        form = GeeksForm(instance=obj)
        context["Form"] = form
        return render(request, "geeks/update_view.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(GeeksModel, id=id)
    obj.delete()
    context["prueba"] = GeeksModel.objects.all()
    return HttpResponseRedirect("/geeks/list", context)


def calc(request):
    return render(request, 'geeks/calc.html')

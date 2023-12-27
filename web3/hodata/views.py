from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from yandexgptlite import YandexGPTLite





def list_objects(request):
    persons = Person.nodes.all()
    cars = Car.nodes.all()
    search_query = request.GET.get('search', '')
    if search_query:
        persons = Person.nodes.filter(name__icontains=search_query)
        cars = Car.nodes.filter(name__icontains=search_query)


    return render (request, 'web3/list_objects.html', {
                                                                            'data': persons,
                                                                            'data_cars': cars,

                                                                            })

def person_new(request):
    if request.method == "GET":
        ps_form = PersonForm()
        return render(request, 'web3/person_new.html', {'ps_form': ps_form} )
    else:
        ps_form = PersonForm(request.POST, request.FILES)
        if ps_form.is_valid():
            person = ps_form.save(commit=False)
            person.save()
            return redirect('list_objects')

def person_update(request, uid):
    person = Person.nodes.get_or_none(uid=uid)
    ps_form = PersonForm(request.POST or None, instance=person)
    if ps_form.is_valid():
        ps_form.save()
        return redirect(list_objects)
    return render(request, "web3/person_update.html", {'ps_form': ps_form})

def car_new(request):
    if request.method == "GET":
        c_form = CarForm()
        return render(request, 'web3/car_new.html', {'c_form': c_form} )
    else:
        c_form = CarForm(request.POST)
        if c_form.is_valid():
            car = c_form.save(commit=False)
            car.save()
            return redirect (list_objects)

def car_update(request, uid):
    car = Car.nodes.get_or_none(uid=uid)
    c_form = CarForm(request.POST or None, instance=car)
    if c_form.is_valid():
        c_form.save()
        return redirect(list_objects)
    return render(request, "web3/car_update.html", {'c_form': c_form})


def list_detail(request, uid):
    persons = Person.nodes.get(uid=uid)
    return render(request, 'web3/list_detail.html', {
                                                                            'person': persons,
                                                                        })
def list_detail_car(request, uid):
    cars = Car.nodes.get(uid=uid)
    return render(request, 'web3/list_detail.html', {
                                                                            'cars': cars,
                                                                        })

def person_delete(request, uid):
    person = Person.nodes.get_or_none(uid=uid).delete()
    return redirect('list_objects')

def car_delete(request, uid):
    car = Car.nodes.get_or_none(uid=uid).delete()
    return redirect('list_objects')


# def zapros(request):
#     if request.method == 'POST':
#         form_real2 = ListItemForm2(request.POST)
#         if form_real2.is_valid():
#             selected_item_person = form_real2.cleaned_data['items_person']
#         else:
#             selected_item_person = None
#     else:
#         form_real2 = ListItemForm2()
#         selected_item_person = None
#
#     context= {
#         'form_real2': form_real2,
#         'selected_item_person': selected_item_person,
#     }
#     return render(request, 'web3/search.html', context)
#
# def zapros3(request):
#     if request.method == 'POST':
#         form_real3 = ListItemForm3(request.POST)
#         if form_real3.is_valid():
#             selected_item_car = form_real3.cleaned_data['items_car']
#         else:
#             selected_item_car = None
#     else:
#         form_real3 = ListItemForm3()
#         selected_item_car = None
#
#     context= {
#         'form_real3': form_real3,
#         'selected_item_car': selected_item_car,
#     }
#     return render(request, 'web3/search.html', context)


def run(requests, Person):
    pers = Person.persons.connect(Person)
    context = {
                'pers':pers,
                }
    return redirect(requests, list_objects, context)

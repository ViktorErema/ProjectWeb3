from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *






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
            return redirect(list_objects)

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
            return redirect(list_objects)

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



def Relationship_person (request):

    person1 = Person.nodes.get()
    person2 = Person.nodes.get()
    return HttpResponse(f"<h2>Name: {person1.persons.connect(person2)} </h2>")


def generate_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        api_key = 'ajeapv6cu1bmq5u6qgnq'

        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        data = {'key': api_key, 'text': input_text, 'lang': 'en-ru'}

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            generated_text = response.json()['text'][0]
            return JsonResponse({'generated_text': generated_text})
        else:
            return JsonResponse({'error': 'Failed to generate text'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


#
# db = django_db.connect()
# cursor = db.cursor()
# cursor.execute("SELECT * FROM mytable")
# results = cursor.fetchall()
# db.close()
# template_name = 'my_app/my_template.html'
#
# def my_view(request):
#     data = {
#         'results': results,
#     }
#     return render(request, template_name, data)
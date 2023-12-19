from itertools import chain

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from neo4j import GraphDatabase
from .forms import *
from .models import *



def document_list(request):
    documents = Document.objects.all()
    return render (request, 'web3/document_list.html', {'items': documents,
                                                                             })

def document_detail(request,document_pk):
    documents = Document.objects.get(pk=document_pk)
    return render(request, 'web3/document_detail.html', {'doc': documents})

def document_new(request):
    if request.method == "GET":
        form = DocumentForm()
        return render(request, 'web3/document_new.html', {'form': form} )
    else:
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            return redirect(document_list)

def zapros2(request):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            selected_item = form.cleaned_data['item']
        else:
            selected_item = None
    else:
        form = ListItemForm()
        selected_item = None

    context= {
        'form': form,
        'selected_item': selected_item,
    }
    return render(request, 'web3/document_list.html', context)

def list_objects(request):
    persons = Person.nodes.all()
    cars = Car.nodes.all()
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

def person_update(request, uid):
    person = Person.nodes.get_or_none(uid=uid)

    ps_form = PersonForm(request.POST or None, instance=person)
    if ps_form.is_valid():
        ps_form.save()
        return redirect(list_objects)
    return render(request, "web3/person_update.html", {'ps_form': ps_form})

# def search(request):
#     results = []
#     if request.method == "GET":
#      query = request.GET.get('search')
#     if query == '':
#      query = 'None'
#     results = Person.nodes.filter(name__icontains=search_query)
#     return render(request," web3/list_objects.html", {'results': results})

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


# class Neo4jConnection:
#     def __init__(self):
#         self.driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "neo4jneo4j"))
#
#     def close(self):
#         if self.driver is not None:
#             self.driver.close()
#
#     def query(self, query, db=None):
#         assert self.driver is not None, "Driver not initialized!"
#         session = None
#         response = None
#         try:
#             session = self.driver.session(database=db) if db is not None else self.driver.session()
#             response = list(session.run(query))
#         except Exception as e:
#             print("Query failed:", e)
#         finally:
#             if session is not None:
#                 session.close()
#         return response
#
# query_string = '''
# LOAD CSV WITH HEADERS FROM
# 'https://raw.githubusercontent.com/Mario-cartoon/bd/main/Product.csv'
# AS line FIELDTERMINATOR ','
# MERGE (product:Product {productID: line.ProductID})
#   ON CREATE SET product.productName = line.ProductName, product.UnitPrice = toFloat(line.UnitPrice);
# '''
# conn.query(query_string, db='graphDb')
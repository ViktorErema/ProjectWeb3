from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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

# def person_update(request, uid, template_name='neo4j_api/person_form.html'):
#     #person = get_object_or_404(Person, uid=uid)
#     person = Person.nodes.get_or_none(uid=uid)
#     if person:
#         print("person = ", person)
#         #name = person.name
#     form = PersonForm(request.POST or None, instance=person)
#     if form.is_valid():
#         form.save()
#         return redirect('neo4j_api:person_list')
#     return render(request, template_name, {'form':form})
#
# def person_list(request, template_name='neo4j_api/person_list.html'):
#
#     person = Person.nodes.all()
#     data = {}
#     data['object_list'] = person
#     return render(request, template_name, data)
#
# def movie_list(request, template_name='neo4j_api/movie_list.html'):
#
#     movie = Movie.nodes.all()
#     data = {}
#     data['object_list'] = movie
#     return render(request, template_name, data)
#
# def get_persons(request):
#
#     #return render('neo4j/persons.html', request, {'persons': Person.nodes.all()})
#     #output = '{}'.format(Person.nodes.all())
#     output = Person.nodes.all()
#     return HttpResponse(output)
#
#
# def persons(request):
#     #return render(request, 'neo4j/persons.html', {'persons': Person.nodes.all()})
#     #return render(request, {'persons': HttpResponse(Person.nodes.all())})
#     return HttpResponse(Person.nodes.all())
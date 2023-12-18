from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def document_list(request):
    documents = Document.objects.all()
    return render (request, 'web3/document_list.html', {'items': documents,
                                                                             })
def person_list(request):
    persons = Person.nodes.all()
    return render (request, 'web3/person_list.html', {
                                                                            'data': persons,
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




def person_update(request, uid):
    person = Person.nodes.get_or_none(uid=uid)
    if person:
     ps_form = PersonForm(request.POST or None, instance=person)
    if ps_form.is_valid():
        ps_form.save()
        return redirect('web3/person_list')
    return render(request, {'ps_form':ps_form})


def person_new(request):
    if request.method == "GET":
        ps_form = PersonForm()
        return render(request, 'web3/person_new.html', {'ps_form': ps_form} )
    else:
        ps_form = PersonForm(request.POST)
        if ps_form.is_valid():
            person = ps_form.save(commit=False)
            person.save()
            return redirect(person_list)
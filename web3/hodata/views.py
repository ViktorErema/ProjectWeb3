from django.shortcuts import render, redirect, get_object_or_404

from .forms import DocumentForm, ListItemForm
from .models import *


def document_list(request):
    documents = Document.objects.all()
    return render (request, 'web3/document_list.html', {'items': documents})

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

# def zapros (request, document_pk):
#     documents = Document.objects.get(pk=document_pk)
#     return render(request, 'web3/document_detail.html', {
#                                                         'items': documents,
#                                                                         })

def zapros(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            selected_item = form.cleaned_data['item']
            return render(request, 'web3/document_list.html', {'item': selected_item})
    else:
        form = DocumentForm()
    return render(request, 'web3/document_list.html', {'form': form})


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

# def get_books(request):
#     return render('web3/document_list.html', request, {'books': Book.nodes.all()})
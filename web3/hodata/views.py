import os.path

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import DocumentForm
from .models import Document


def document_new(request):
    if request.method == 'GET':
        form = DocumentForm
        return render(request, 'web3/document_new.html', {'form': form})
    else:
        form = DocumentForm(request.DOCUMENT, request.FILES)
        if form.is_valid():
            return redirect('document_list', documen_pk=document.pk)


def document_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        document = Document.objects.filter(title__icontains=search_query)
    context = {'items': document,
               }
    return render(request, 'web3/document_list.html', context)
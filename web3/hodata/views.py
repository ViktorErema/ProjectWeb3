from django.shortcuts import render, redirect

from .forms import DocumentForm
from .models import Document


def document_list(request):
    documents = Document.objects.all()
    return render (request, 'web3/document_list.html', {'items': documents})

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


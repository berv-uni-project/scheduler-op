from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UploadFileForm
from .models import Document

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            methode = form.cleaned_data['radiobutton']
            # Redirect to the document list after POST
            return HttpResponseRedirect('/load/?methode='+methode)
    else:
        form = UploadFileForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

def about(request):
    return render(request, 'about.html')

def loading(request):
    document = Document.objects.all().last();
    methode = request.GET.get('methode')
    return render(request, 'run.html', {'document':document, 'methode':methode})
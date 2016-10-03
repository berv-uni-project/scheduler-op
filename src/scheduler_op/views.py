from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import os.path
import platform

from .forms import UploadFileForm
from .models import Document
from scheduler_op.hill_climbing import *
from scheduler_op.simulated_annealing import *
from scheduler_op.genetic_algorithm import *
from scheduler_op.bacafilez import *
from scheduler_op.class_cons import *

def list(request):
    # Handle file upload
    documents = Document.objects.all()
    for document in documents:
        document.delete()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(id=1,docfile=request.FILES['docfile'])
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
    methode = request.GET.get('methode')
    return HttpResponseRedirect('/result/?methode='+methode)

def result(request):
    document = Document.objects.all().last()
    methode = request.GET.get('methode')
    SITE_ROOT = os.path.join(settings.BASE_DIR, 'scheduler_op/media/')
    docum = os.path.join(SITE_ROOT+document.docfile.name)
    system = platform.system()
    if (system=="Windows"):
        docum = docum.replace('/','\\')
    print(docum)
    b = Bacafile()
    c = allcourse(docum, b)
    a = allroom(docum, b)
    if (methode == 1) :
        X = simulated_annealing(c, a, 1)
        X.simulate()
        #simulated anealing
    elif (methode == 2) :
        X = genetic_algorithm(c, a, 4)
        X.genetic_start()
        #genetic algorithm
    else :
        X = hillclimbing(c, a)
        X.start()
        #default hill climbing

    conflict = str(gettotalconflict(X.var))
    return render(request,'result.html',{'X':X,'conflict':conflict});
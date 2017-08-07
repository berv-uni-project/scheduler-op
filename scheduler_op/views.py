import os.path
import platform

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

from scheduler_op.bacafilez import *
from scheduler_op.genetic_algorithm import *
from scheduler_op.simulated_annealing import *
from .forms import UploadFileForm
from .models import Document


# render home page
def list(request):
    # Handle file upload

    documents = Document.objects.all()
    maxID = 0
    for document in documents:
        if (document.id > maxID):
            maxID = document.id

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_id = maxID + 1
            newdoc = Document(file_id, docfile=request.FILES['docfile'])
            newdoc.save()
            methode = form.cleaned_data['radiobutton']
            # Redirect to the document list after POST
            return HttpResponseRedirect('/load/?methode=' + methode + "&file_id=" + str(file_id))
    else:
        form = UploadFileForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )


# render about page
def about(request):
    return render(request, 'about.html')


# transient page
def loading(request):
    methode = request.GET.get('methode')
    doc_id = request.GET.get('file_id')
    return HttpResponseRedirect('/result/?methode=' + methode + "&file_id=" + str(doc_id))


# render result page
def result(request):
    methode = request.GET.get('methode')
    doc_id = request.GET.get('file_id')
    document = Document.objects.get(id=doc_id)
    SITE_ROOT = os.path.join(settings.BASE_DIR, 'scheduler_op/media/')
    docum = os.path.join(SITE_ROOT + document.docfile.name)
    system = platform.system()
    # TODO : If not supported format, throw to exception page
    if system == "Windows":
        docum = docum.replace('/', '\\')

    if docum.endswith('.txt'):
        b = Bacafile()
        c = allcourse(docum, b)
        a = allroom(docum, b)
        if (methode == 1):
            X = simulated_annealing(c, a, 0.8)
            X.simulate()
            # simulated anealing
        elif (methode == 2):
            X = genetic_algorithm(c, a, 400)
            X.genetic_start()
            # genetic algorithm
        else:
            X = hillclimbing(c, a)
            X.start()
            # default hill climbing

        conflict = str(gettotalconflictpersks(X.var))
        return render(request, 'result.html',
                      {'X': X, 'conflict': conflict, 'allroom': a.roomlist, 'time': range(7, 18), 'day': range(1, 6),
                       'invalid_course': invalid_course})
    else:
        return render(request, 'error.html')

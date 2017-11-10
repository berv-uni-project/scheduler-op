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
from .contributor import Contributor


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
    contributors = []
    bervi = Contributor(name='Bervianto Leo Pratama', nim=13514047, image='images/bervi-135.jpg',facebook='https://facebook.com/bervianto.leo', github='https://github.com/berviantoleo', linkedin='https://www.linkedin.com/in/bervianto-leo-pratama')
    jeje = Contributor(name='Jeremia Jason Lasiman', nim=13514021, image='images/jeje-135.jpg')
    zahid = Contributor(name='M. Az-zahid Adhitya S.', nim=13514095, image='images/zahid-135.jpg')
    richard = Contributor(name='Richard Wellianto', nim=13514051, image='images/richard-135.jpg')
    amir = Contributor(name='Amir', nim=13514017, image='images/amir-135.jpg')
    contributors.append(amir)
    contributors.append(jeje)
    contributors.append(bervi)
    contributors.append(richard)
    contributors.append(zahid)
    return render(request, 'about.html', {'contributors': contributors})


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
        is_checked = b.checkFormat(docum)
        if is_checked:
            c = allcourse(docum, b)
            a = allroom(docum, b)
            if a.maxID()> 0 and c.maxID() > 0:
                if methode == 1:
                    X = simulated_annealing(c, a, 0.8)
                    X.simulate()
                    # simulated anealing
                elif methode == 2:
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
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Batiment

from batiment.forms import BatimentForm

def list(request):
    batiments = Batiment.objects.prefetch_related('etages__locals').all()
    return render(request, 'batiment/list.html', {'batiments': batiments})

def show(request,pk):
    batiment=get_object_or_404(Batiment,pk=pk)
    return render(request,'batiment/show.html',{'batiment':batiment })

from django.shortcuts import render, redirect
from .forms import BatimentForm

def new(request):
    if request.method == 'POST':
        form = BatimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batiment_list')
    else:
        form = BatimentForm()
    return render(request, 'batiment/new.html', {'form': form})


def edit(request,pk):
    batiment=get_object_or_404(Batiment,pk=pk)
    if request.method == 'POST':
        form = BatimentForm(request.POST, instance=batiment)  # remplit le formulaire existant
        if form.is_valid():
            form.save()  # sauvegarde les modifications
            return redirect('batiment_list')
    else:
        form = BatimentForm(instance=batiment)  # formulaire pré-rempli

    return render(request, 'batiment/edit.html', {'form': form, 'batiment': batiment})

def delete(request,pk):
    batiment=get_object_or_404(Batiment,pk=pk)
    return render(request,'batiment/delete.html', {'batiment': batiment})

def treeview_batiment(request, pk):
    batiment = get_object_or_404(Batiment, pk=pk)
    return render(request, 'batiment/treeview.html', {'batiment': batiment})



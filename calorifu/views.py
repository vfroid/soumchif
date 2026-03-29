from django.shortcuts import render, get_object_or_404,redirect

from .models import Calorifu
from .forms import CalorifuForm

def list(request):
    calorifus = Calorifu.objects.all()
    return render(request, 'calorifu/list.html', {'calorifus': calorifus})


def new(request):
    if request.method == 'POST':
        calorifu=Calorifu()
        form=CalorifuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calorifu_list')
    else:
        form = CalorifuForm()
    return render(request,'calorifu/new.html',{'form':form})

def edit(request,pk):
    calorifu=get_object_or_404(Calorifu,pk=pk)
    if request.method == 'POST':
        form = CalorifuForm(request.POST, instance=calorifu)
        if form.is_valid():
            form.save()
            return redirect('calorifu_list')
    else:
        form = CalorifuForm(instance=calorifu)
    return render(request, 'calorifu/edit.html', {'form': form, 'calorifu':calorifu})


def show(request, pk):
    calorifu = get_object_or_404(Calorifu, pk=pk)
    return render(request, 'calorifu/show.html', {'calorifu': calorifu})

def delete(request, pk):
    calorifu = get_object_or_404(Calorifu, pk=pk)
    if request.method == 'POST':
        calorifu.delete()  # supprime l'équipement
        return redirect('calorifu_list')
    return render(request, 'calorifu/delete.html', {'calorifu': calorifu})




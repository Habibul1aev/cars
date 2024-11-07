from django.shortcuts import render, redirect, get_object_or_404
from cars.models import Cars
from workspace.forms import CarCreate

def main(request):
    cars = Cars.objects.all()

    return render(request, 'workspace/body.html', {'cars':cars})


def create(request):
    form = CarCreate()
    if request.method == 'POST':
        form = CarCreate(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = form.save()
            
        return redirect('/workspace/')


    return render(request, 'workspace/create.html', {'form':form})

def update(req, id):
    car = get_object_or_404(Cars, id=id)
    if req.method == 'POST':
        form = CarCreate(data=req.POST, files=req.FIELS, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('/workspace/')

    else:
        form = CarCreate(instance=car)

    return render(req, 'workspace/update.html', {'form':form, 'car': car})

def delete(req, id):
    car = Cars.objects.get(id=id)
    car.delete()

    return redirect('/workspace/')
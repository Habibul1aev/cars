from django.shortcuts import render
from cars.models import Cars, Category, Hesh

def main(request):
    cars = Cars.objects.all()

    search = request.GET.get('search')
    if search:
        cars = cars.filter(name__icontains=search)

    category = request.GET.get('category')
    if category:
        category = Category.objects.get(id=int(category))
        cars = cars.filter(category=category)
    
    category_list = Category.objects.all()
    return render(request, 'index.html', {'cars' : cars, 'category_list' : category_list})

def obzor(request, id):
    cars = Cars.objects.get(id=id)
    cars.views += 1
    cars.save()
    category_list = Category.objects.all()
    return render(request, 'obzor.html', {'cars': cars, 'category_list': category_list})



'контекст'
'queryparams'

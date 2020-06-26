from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Toys
from .forms import ToyCreate
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.


def index(request):
    shelf = Toys.objects.all()
    return render(request, 'library.html', {'shelf': shelf})
def upload(request):
    upload = ToyCreate()
    if request.method == 'POST':
        upload = ToyCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})
def update_toy(request, toy_id):
    toy_id = int(toy_id)
    try:
        toy_sel = Toys.objects.get(id = toy_id)
    except Toys.DoesNotExist:
        return redirect('index')
    toy_form = ToyCreate(request.POST ,request.FILES, instance = toy_sel)
    if toy_form.is_valid():
       toy_form.save()
       return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':toy_form})
def delete_toy(request, toy_id):
    toy_id = int(toy_id)
    try:
        toy_sel = Toys.objects.get(id = toy_id)
    except Toys.DoesNotExist:
        return redirect('index')
    toy_sel.delete()
    return redirect('index')
class SearchResultsView(ListView):
    model = Toys
    template_name = 'libary-search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Toys.objects.filter(
            Q(name__icontains=query) | Q(describe__icontains=query)
        )
        return object_list
from django.shortcuts import redirect, render
from .models import item
from shop.forms import ItemForm

# Create your views here.
def item_list(request):
    context = {'item_list': item.objects.all()}
    return render(request, 'shop/item_list.html',context)

# GET AND POST request (insert or update operations)
def item_form(request):
    if request.method == 'GET':
        # GET request
        form = ItemForm()
        return render(request, 'shop/item_form.html', {'form': form})
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            # POST request
            form.save()
        return redirect('/shop/list')
   
#  DELETE request (delete operations)
def item_delete(request):
    return render(request, '')


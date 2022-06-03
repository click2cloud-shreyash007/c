from django.shortcuts import redirect, render
from .models import item
from shop.forms import ItemForm

# Create your views here.
def item_list(request):
    context = {'item_list': item.objects.all()}
    return render(request, 'shop/item_list.html',context)

# GET AND POST request (insert or update operations)
def item_form(request,item_id=0):
    if request.method == 'GET':
        # GET request
        if item_id==0: # insert operation
            form = ItemForm()
        else: #update operation
            i = item.objects.get(pk=item_id)
            form = ItemForm(instance=i)
            
        return render(request, 'shop/item_form.html', {'form': form})
    else:
        if item_id == 0:
            form = ItemForm(request.POST)
        else:
            i = item.objects.get(pk=item_id)
            form = ItemForm(request.POST, instance=i)
        if form.is_valid():
            # POST request
            form.save()
        return redirect('/shop/list')
   
#  DELETE request (delete operations)
def item_delete(request,item_id=0):
    i = item.objects.get(pk=item_id)
    i.delete()
    return redirect('/shop/list')


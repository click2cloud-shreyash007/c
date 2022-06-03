from django.shortcuts import render

from shop.forms import ItemForm

# Create your views here.
def item_list(request):
    return render(request, 'shop/item_list.html')

# GET AND POST request (insert or update operations)
def item_form(request):
    form = ItemForm()
    return render(request, 'shop/item_form.html',{'form':form})

#  DELETE request (delete operations)
def item_delete(request):
    return render(request, '')


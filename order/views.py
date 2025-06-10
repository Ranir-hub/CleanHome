from django.shortcuts import render
from catalogue.models import Item
from order.models import Order
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from order import forms

# Create your views here.
@login_required(login_url = 'accounts:login')
def order_list(request):
    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(id_Customer = request.user)
    return render(request, 'order/order_list.html', {'orders' : orders})

@login_required(login_url = 'accounts:login')
def order(request, slug):
    order = Order.objects.get(slug = slug)
    if request.user.id == order.id_Customer:
        return render(request, 'order/order.html', {'order' : order})
    else:
        return HttpResponse('401 Unauthorized', status = 401)

@login_required(login_url = 'accounts:login')
def order_create(request, slug):
    items = Item.objects.all()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_Customer = request.user
            instance.save()
            return redirect('order:order_list')
    else:
        form = forms.OrderForm()
    return render(request, 'order/order_form.html', {'form' : form, 'items' : items})

@login_required(login_url='accounts:login')
def order_update(request, slug):
    order = Order.objects.get(slug = slug)
    items = Item.objects.all()
    if request.user.id == order.id_Customer.id:
        if request.method == 'POST':
            form = forms.OrderForm(request.POST, instance = order)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect('order:order')
        else:
            form = forms.OrderForm(instance=order)
        return render(request, 'order/order_update_delete.html', {'form' : form, 'order' : order})
    return HttpResponse('401 Unauthorized', status = 401)

@login_required(login_url='accounts:login')
def order_delete(request, slug):
    order = Order.objects.get(slug=slug)
    if request.user.id == order.id_Customer.id:
        if request.method == 'POST':
            order.delete()
            return redirect('order:order_list')
        return render(request, 'catalogue/catalogue_confirm_delete.html', {'order': order})
    return HttpResponse('401 Unauthorized', status = 401)



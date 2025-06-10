from django.shortcuts import render
from catalogue.models import Item, Category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from catalogue import forms

def catalogue(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'catalogue/catalogue.html', {'items' : items, 'categories' : categories})

def category(request):
    categories = Category.objects.all()
    return render(request, 'catalogue/categories.html', {'categories' : categories})

def item(request, slug):
    items = Item.objects.all()
    item = Item.objects.get(slug=slug)
    return render(request, 'catalogue/item.html', {'items' : items, 'item':item})

def category_this(request, slug):
    category = Category.objects.get(slug = slug)
    items = Item.objects.filter(id_category = category)
    categories = Category.objects.all()
    return render(request, 'catalogue/catalogue.html', {'items' : items, 'categories' : categories})

@login_required(login_url = 'accounts:login')
def item_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.ItemForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect('catalogue:list')
        else:
            form = forms.ItemForm()
    return render(request, 'catalogue/catalogue_form.html', {'form' : form})

@login_required(login_url='accounts:login')
def item_update(request, slug):
    item = Item.objects.get(slug=slug)
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.ItemForm(request.POST, request.FILES, instance = item)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect('catalogue:item', slug=item.slug)
        else:
            form = forms.ItemForm(instance=item)
        return render(request, 'catalogue/catalogue_form.html', {'form': form})
    return HttpResponse('401 Unauthorized', status = 401)

@login_required(login_url='accounts:login')
def item_delete(request, slug):
    item = Item.objects.get(slug=slug)
    if request.user.is_staff:
        if request.method == 'POST':
            item.delete()
            return redirect('catalogue:list')
        return render(request, 'catalogue/catalogue_confirm_delete.html', {'item': item})
    return HttpResponse('401 Unauthorized', status = 401)

@login_required(login_url = 'accounts:login')
def category_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.CategoryForm(request.POST)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect('catalogue:list')
        else:
            form = forms.CategoryForm()
    return render(request, 'catalogue/catalogue_form.html', {'form' : form})

@login_required(login_url='accounts:login')
def category_update(request, slug):
    category = Category.objects.get(slug=slug)
    if request.user.is_staff:
        if request.method == 'POST':
            form = forms.CategoryForm(request.POST, instance = category)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.save()
                return redirect('catalogue:list')
        else:
            form = forms.CategoryForm(instance=category)
        return render(request, 'catalogue/category_update_delete.html', {'form': form, 'category' : category})
    return HttpResponse('401 Unauthorized', status = 401)

@login_required(login_url='accounts:login')
def category_delete(request, slug):
    category = Category.objects.get(slug=slug)
    if request.user.is_staff:
        if request.method == 'POST':
            category.delete()
            return redirect('catalogue:list')
        return render(request, 'catalogue/catalogue_confirm_delete.html', {'category': category})
    return HttpResponse('401 Unauthorized', status = 401)

from django.shortcuts import render, redirect

from examproject.core.utils import get_user, get_all_items
from examproject.exam.forms import CreateProfileForm, CreateItemForm, EditItemForm, DeleteItemForm, DeleteProfileForm
from examproject.exam.models import Item


# Create your views here.


def index(request):
    user = get_user()
    items = get_all_items()
    context = {
        'user': user,
        'items': items,
    }
    if user:
        return render(request, 'home-with-profile.html', context)

    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # form.full_clean()
            form.save()
            return redirect('index')

    context = {
        'user': user,
        'form': form,
        'items': items,
    }
    return render(request, 'home-no-profile.html', context)


def add_item(request):

    form = CreateItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # form.full_clean()
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def details_item(request, id):
    item = Item.objects.get(id=id)

    context = {
        'item': item
    }
    return render(request, 'album-details.html', context)


def edit_item(request, id):
    item = Item.objects.get(id=id)

    form = EditItemForm(instance=item)
    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=item)
        if form.is_valid():
            # form.full_clean()
            form.save()
            return redirect('index')

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_item(request, id):
    item = Item.objects.get(id=id)

    form = DeleteItemForm(instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('index')

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'delete-album.html', context)


# Profile views

def details_profile(request):
    user = get_user()
    item_count = Item.objects.count()

    context = {
        'user': user,
        'item_count': item_count,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    user = get_user()

    form = DeleteProfileForm(instance=user)
    if request.method == 'POST':
        Item.objects.all().delete()
        user.delete()
        return redirect('index')

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
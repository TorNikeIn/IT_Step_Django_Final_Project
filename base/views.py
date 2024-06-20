from django.shortcuts import render, redirect, get_object_or_404
from .models import Website, Category
from .forms import WebsiteForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'base/category_list.html', {'categories': categories})

def website_list_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    websites = Website.objects.filter(category=category)
    return render(request, 'base/website_list.html', {'category': category, 'websites': websites})



def home(request):
    websites = Website.objects.all()
    context = {'websites': websites}
    return render(request, 'base/home.html', context)
#
#
def website(request, pk):
    website = Website.objects.get(id=pk)
    context = {'website': website}
    return render(request, 'base/website.html', context)



def createCatalog(request):
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/catalog_form.html', context)


def edit_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    if request.method == 'POST':
        form = WebsiteForm(request.POST, instance=website)
        if form.is_valid():
            form.save()
            return redirect('website_list_by_category', category_name=website.category.name)
    else:
        form = WebsiteForm(instance=website)
    return render(request, 'base/edit_website.html', {'form': form, 'website': website})

def delete_website(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    category_name = website.category.name
    if request.method == 'POST':
        website.delete()
        return redirect('website_list_by_category', category_name=category_name)
    return render(request, 'base/confirm_delete.html', {'website': website})


from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageForm
from .models import ProductImage


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save()
            for image in request.FILES.getlist('image'):
                ProductImage.objects.create(product=product, image=image)
            return redirect('success_page')  # Redirect to a success page
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'add_product.html', {'product_form': product_form, 'image_form': image_form})

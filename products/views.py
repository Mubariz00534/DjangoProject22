from django.shortcuts import render, get_object_or_404, Http404
from django.views import generic
from .models import Product

class ProductListView(generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'product_lists'

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generic.DetailView):
    template_name = 'products/detail.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     ###########################################
#     # product = None

#     # qs = Product.objects.filter(pk=pk)
#     # if qs.exists() and qs.count() == 1:
#     #     product = qs.first()
#     # else:
#     #     raise Http404("Bele bir product tapilmadi!!!")
#     ###############################################

#     context = {
#         'product': product
#     }

#     return render(request, 'products/detail.html', context)

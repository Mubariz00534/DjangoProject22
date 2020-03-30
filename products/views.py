from django.shortcuts import render, get_object_or_404, Http404
from django.views import generic
from .models import Product

class ProductFeaturedListView(generic.ListView):
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductFeaturedListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self):
        return Product.objects.featured().active()

class ProductFeaturedDetailView(generic.DetailView):
    template_name = 'products/featured-detail.html'
    
    def get_queryset(self):
        return Product.objects.featured()



class ProductListView(generic.ListView):
    template_name = 'products/list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()

    # queryset = Product.objects.all()

class ProductDetailSlugView(generic.DetailView):
    template_name = 'products/detail.html'
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Product Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except: 
            raise Http404("Basqa bir prob. cixdi!!")
        return instance

# class ProductDetailView(generic.DetailView):
#     template_name = 'products/detail.html'
#     # model = Product

#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         print(context)
#         return context

#     def get_object(self, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         instance = Product.objects.get_by_id(pk)
#         if instance is None:
#             return Http404("Product Not Found")
#         return instance

#     # def get_queryset(self, *args, **kwargs):
#     #     pk = self.kwargs.get('pk')
#     #     return Product.objects.filter(pk=pk)

    
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

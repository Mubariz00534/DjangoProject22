from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='products-detail'),
    # path('<int:pk>/', views.product_detail_view, name='products-detail'),
]
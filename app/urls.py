from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^display/$',views.Display.as_view(), name='display'),
    url(r'^display1/$',views.Display1.as_view(),name='display'),
    url(r'^caty/products/$', views.CategoryProducts.as_view(), name='category-products'),
    url(r'^products/$', views.SubcategoryProduct.as_view(),name='subcategory-products'),
]
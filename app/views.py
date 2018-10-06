from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Category, Product,Sub_Category
from rest_framework.response import Response
from .serializer import CategorySerializer, ProductSerializer,SubCategorySerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.

class Display(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Display1(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'

    def get(self,request):
        queyset = Category.objects.all()
        return Response({'category':queyset})


class CategoryProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    print(renderer_classes,'Hiiiiiiiii')
    # template_name = 'mypage.html'

    def get(self,request):
        print('i am in view')
        obj = Category.objects.all()
        # obj1 = Sub_Category.objects.all()
        li = []
        pi = []
        for i in obj:
            cat_id=i.pk
            print(cat_id)
            queryset = Sub_Category.objects.filter(category= cat_id)

            print('$$$$$$$',queryset)
            for j in queryset:
                sub_cat_id = j.pk
                pro_obj = Product.objects.filter(sub_category=sub_cat_id)
                for k in pro_obj:
                    print("li before", li)
                    li.append({
                        'category': k.sub_category.category.category_name,
                        'sub_category': k.sub_category .sub_category_name,
                        'product_name': k.product_name
                    })
                    print("name",k.product_name)

                    # li.append(df)
                    print("li after",li)

        #         pro_obj = Product.objects.filter(pk=sub_cat_id)
        #         for k in pro_obj:
        #             lk={}
        #             lk['product'] = k.product_name
        #         # pro_name = j.product_name
        #         # sub_cat_name=j.product_id.sub_category_name
        #         # cat_name=j.product_id.sub_category_id.category_name
        #         # df[cat_name] = sub_cat_name
        #         # # df['pro_name'] = pro_name
        #             df.append(lk)
        #     li.append(df)
        # print('^^^^^^^',li)
        return render_to_response('mypage.html',{'li':li})

class SubcategoryProduct(APIView):
    print('I am in Subcategory APi display')
    serializer_class = ProductSerializer

    def get_queryset(self):
        print('I am in function')
        cat_id = self.kwargs.get('pk', None)
        print(cat_id)
        if cat_id is not None:
            print('I am in if function')
            category = get_object_or_404(Category, category_id=cat_id)
            return Product.objects.filter(
                categories__path__startswith=category.path
            ).all()
        else:
            return Product.objects.none()



    # def get(self,request):
    #     print('I am in subcategory view')
    #     obj = Sub_Category.objects.all()
    #     print('GYHHHGDHD',obj)
    #     li = []
    #     for i in obj:
    #         print('I am in for loop')
    #         sub_cat_id = str(i.sub_category_name)
    #         print('Mahima', sub_cat_id)
    #         queryset = Product.objects.filter(product_id = sub_cat_id)
    #         print('*************', queryset)
    #         for j in queryset:
    #             df ={}
    #             sub_name = j.sub_category_name
    #             pro_name = j.sub_category_name.product_name
    #             df[pro_name] = sub_name
    #             li.append(df)
    #     print('%%%%%%%%', li)
    #     return render({'li':li})
#
#
#
# # class CategoryProductsView(generics.ListAPIView):
# #     print('I am in class')
# #     serializer_class = ProductSerializer
# #     queryset = Product.objects.all()
# #
# #     def mypage(request):
# #         print('I am in view')
# #         details = Product.objects.select_related().all()
# #         names = [d.product_name for d in details]
# #         info = zip(names,details)
# #
# #         return render(request,'mypage.html',{'info':info})






from django.shortcuts import render,redirect
from app.models import slider , banner_area, Main_Category, Product

def Base(request):
    return render(request,'base.html')


def HOME(request):

    sliders = slider.objects.all().order_by('-id')[0:3] # ye humne id se sliders model ke teen data ko fech kiya he vo bhi revers me yani niche se uparki taraf
    banner_areas = banner_area.objects.all().order_by('-id')[0:3]

    main_category = Main_Category.objects.all().order_by('-id')
    product = Product.objects.filter(section__name ="Top Deals Of The Day")
    print(product)

    Context = {
        'slider':sliders,
        'banner_area':banner_areas,
        'main_category':main_category,
        'product':product,
    }
    return render(request,'Main/home.html',Context)


def testpage(request):

    return render(request,'test1.html')


def PRODUCT_DETAILS(request,slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product':product
    }
    return render(request,"product/product_detail.html",context)
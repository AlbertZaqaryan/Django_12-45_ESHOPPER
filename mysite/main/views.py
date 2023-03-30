from django.shortcuts import render
from .models import SliderActive, Category, SubCategory
# Create your views here.


def index(request):
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    return render(request, 'main/index.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list
    })


def index_detail(request, id):
    slider_active = SliderActive.objects.all()[0]
    slider = SliderActive.objects.all()[1:]
    category_list = Category.objects.all()
    sub_category_list = SubCategory.objects.all()
    category_filter = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'slider_active':slider_active,
        'slider':slider,
        'category_list':category_list,
        'sub_category_list':sub_category_list,
        'category_filter':category_filter
    })
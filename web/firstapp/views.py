from django.shortcuts import render
from django.http import HttpResponse
from requests import Response
from .models import Car
import pandas as pd
import numpy as np
import csv
import pickle
import os
from django.conf import settings
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
import joblib
from django.views.decorators.csrf import csrf_exempt

reloadModel = joblib.load('./mod/model/gb_6.model')

# Create your views here.

def blog(request) :
    # model = Car.objects.get(id=1)
    # item = {'main_intro' : model.main_intro}
    return render(request, 'blog.html')


def blog2(request) :
    brands = request.POST.get('brand')
    # html파일의 method="post"인 <form>태그를 찾고 그 중에서 name="brand"인 태그의 입력값을 가져오겠다.
    years = request.POST.get('year')
    # html파일의 method="post"인 <form>태그를 찾고 그 중에서 name="year"인 태그의 입력값을 가져오겠다.
    fueltypes = request.POST.get('fuelType')
    ranges = request.POST.get('range')

    # 위에서 받은 변수 값들을 키와 연결시켜 저장
    context = { 'brand':brands, 'year' : years, 'fueltype' : fueltypes , 'range' : ranges }
    return render(request, 'blog2.html', context )

def blog3(request) :
    brands = request.POST.get('brand')
    years = request.POST.get('year')
    fueltypes = request.POST.get('fuelType')
    ranges = request.POST.get('range')

    context = { 'brand':brands, 'year' : years, 'fueltype' : fueltypes , 'range' : ranges }
    return render(request, 'blog3.html', context )

def blog4(request) :
    brands = request.POST.get('brand')
    years = request.POST.get('year')
    fueltypes = request.POST.get('fuelType')
    ranges = request.POST.get('range')

    context = { 'brand':brands, 'year' : years, 'fueltype' : fueltypes , 'range' : ranges }
    return render(request, 'blog4.html', context )

def blog5(request) :
    brands = request.POST.get('brand')
    years = request.POST.get('year')
    fueltypes = request.POST.get('fuelType')
    ranges = request.POST.get('range')

    context = { 'brand':brands, 'year' : years, 'fueltype' : fueltypes , 'range' : ranges }
    return render(request, 'blog5.html', context )

# def service_list(request):
#     Category.objects.create(brand='Audi', year='2020', mileage='15000')
#     return HttpResponse('입력 완료')

# def upload_csv(request):
#     data ={}
#     if "GET" == request.method:
#         return render(request, "firstapp/upload_csv.html", data)

def csv_model(request) :
    path = 'C:/Users/admin/miniP2/mod/data'
    file = open(path)
    reader = csv.reader(file)
    print('----', reader)
    list = []
    for row in reader :
        list.append(Car( brand        = row[0],
                         model        = row[1],
                         year         = row[2],
                         price        = row[3],
                         transmission = row[4],
                         mileage      = row[5],
                         fuelType     = row[6],
                         mpg          = row[7],
                         engineSize   = row[8]))
    Car.objects.bulk_create(list)
    
    return HttpResponse('create model!@')


# class Predict(views.APIView):
#     def post(self, request):
#         predictions = []
#         for entry in request.data:
#             model_name = entry.pop('model_name')
#             path = os.path.join(settings.MODEL_ROOT, model_name)
#             with open(path, 'rb') as file :
#                 model = pickle.load(file)
#             try:
#                 result = model.predict(pd.DataFrame([entry]))
#                 predictions.append(result[0])

#             except Exception as err :
#                 return Response(str(err), status = status.HTTP_400_BAD_REQUEST)
#         return Response(predictions, status=status.HTTP_200_OK)

# def predictP(request):
#     if request.method == 'POST':
#         temp = {}
#         li = ['bmw', 'cclass', 'focus', 'ford', 'hyundi', 'merc', 'skoda', 'toyota', 'vauxhall', 'vw']
#         if request.POST.get('brand') == 'bmw' :
#             temp['brand_bmw'] = 1
#             temp['brand_cclass'] = 0
#             temp['brand_focus'] = 0
#             temp['brand_ford'] = 0
#             temp['brand_merc'] = 0
#             temp['brand_skoda'] = 0
#             temp['brand_toyota'] = 0
#             temp['brand_vauxhall'] = 0
#             temp['brand_vw'] = 0
#         elif request.POST.get('brand') == 'cclass' :
#             temp['brand_bmw'] = 0
#             temp['brand_cclass'] = 1
#             temp['brand_focus'] = 0
#             temp['brand_ford'] = 0
#             temp['brand_merc'] = 0
#             temp['brand_skoda'] = 0
#             temp['brand_toyota'] = 0
#             temp['brand_vauxhall'] = 0
#             temp['brand_vw'] = 0
                   
#         for brand in li :
#             if request.POST.get('brand') == brand :
#                 temp['brand_'+ brand] = 1
#         temp['brand'] = request.POST.get('brand')
#         temp['year'] = request.POST.get('year')
#         temp['fuelType'] = request.POST.get('fuelType')
#         temp['mileage'] = request.POST.get('mileage')
#         temp[''] = request.POST.get('')
#         temp[''] = request.POST.get('')
#         temp[''] = request.POST.get('')
#         temp[''] = request.POST.get('')

#     testData = pd.DataFrame({'x':temp}).transpose()
#     scoreval = reloadModel.predict(testData)[0]
#     context = {'scoreval':scoreval}
#     return render(request, 'blog4.html', context)


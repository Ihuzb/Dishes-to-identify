# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, base64, json, sys
from django.shortcuts import render
from django.http import HttpResponse
from shibie import endover
from django.db import connection
from RickAndMorty.models import Foods

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
def updateImg(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        imgdata = base64.b64decode((request.POST['base64Image']).split(',')[1])
        imgname = request.POST['base64ImageName'].replace('.png', '.jpg')
        with open('media/' + imgname, 'wb') as file:
            file.write(imgdata)
            file.close
        shibiejieguo = endover(imgname)
        FoodDate = []
        for index, n in enumerate(shibiejieguo['date']):
            # foodValue = Foods.objects.get(id=int(n + 1))
            # foodValue = Foods.objects.raw("SELECT * FROM ram.rickandmorty_foods where id=%s" % (str(n + 1)))
            cursor.execute("SELECT * FROM ram.rickandmorty_foods where id=%s" % (str(n + 1)))
            col_names = [desc[0] for desc in cursor.description]
            print col_names
            foodValue = cursor.fetchone()
            foodValue = dict(zip(col_names, foodValue))
            print foodValue
            # del (foodValue.__dict__['_state'])
            value = {'name': shibiejieguo['name'][index],
                     # 'data': {'name': food['name'], 'nutritive': food['nutritive'], 'adapt': food['adapt']}}
                     'data': dict(foodValue)}
            FoodDate.append(value)
        shibiejieguo['over'] = FoodDate
    return HttpResponse(json.dumps(shibiejieguo), content_type='application/json')

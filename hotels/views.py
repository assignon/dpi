from django.shortcuts import render
from django.db.models.query_utils import Q
# from models.user_model import User
import argparse
from django.http import JsonResponse
from .models import *
import csv


# Create your views here.

class InsertCsv:
    def insert_city(self):
        get_cities = City.objects.all().count()
        # open city csv filr in a context manager
        with open('city.csv') as city:
            for cities in city:
                # split the data by ;
                splited_city = cities.split(';')
                # check if data is already insert
                if get_cities == 0:
                    # add data to DB
                    City.objects.create(
                        acronym=splited_city[0],
                        name=splited_city[1]
                    )
                else:
                    print('cities data laready insert')
                    break
            print('city added')

    def insert_hotel(self):
        # open hotels csv filr in a context manager
        get_hotels = Hotel.objects.all().count()
        with open('hotel.csv') as hotel:
            for hotels in hotel:
                # split the data by ;
                splited_city = hotels.split(';')
                # check if data is already insert
                if get_hotels == 0:
                    # add data to DB
                    Hotel.objects.create(
                        city=splited_city[0],
                        region=splited_city[1],
                        name=splited_city[2]
                    )
                else:
                    print('hotel data laready insert')
                    break
            print('hotel added')


def home(request):
    # get cities
    cities = City.objects.all().values()
    regions = Hotel.objects.all().values()

    return render(request, 'hotels/home.html', {'city': cities, 'region': regions})


def get_city_region(request):
    region_arr = []
    city_acronym = request.GET.get('city_acronym')
    regions = Hotel.objects.filter(city=city_acronym).values()

    for r in regions:
        region_arr.append(r['region'])

    # return {'regions': regions}
    return JsonResponse({'regions': region_arr})


def get_hotels(request):
    hotel_arr = []
    hotels = None
    city_acronym = request.GET.get('city_acronym')
    region = request.GET.get('region')

    # filter hotels base on sended parameters
    if region == 'all':
        hotels = Hotel.objects.filter(city=city_acronym).values()
    else:
        hotels = Hotel.objects.filter(
            Q(city=city_acronym) & Q(region=region)).values()

    for h in hotels:
        hotel_arr.append(h)

    return JsonResponse({'hotels': hotel_arr})

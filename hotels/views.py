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
        """insert city csv data in sqlite3 DB
        """
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
        """insert hotel csvb data in sqlite3 DB
        """
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
    print(type(request))
    """display home page

    Args:
        request (WSGIRequest'): [get requested data from user]

    Returns:
        [html page]: [home html view and city and region data from DB]
    """
    # get cities
    cities = City.objects.all().values()
    regions = Hotel.objects.all().values()

    return render(request, 'hotels/home.html', {'city': cities, 'region': regions})


def get_city_region(request):
    """get region data from the DB base on the user requested data

    Args:
        request (dicy): [user requested data]

    Returns:
        [dict]: [region data]
    """
    region_arr = []
    city_acronym = request.GET.get('city_acronym')
    regions = Hotel.objects.filter(city=city_acronym).values()

    for r in regions:
        region_arr.append(r['region'])

    return JsonResponse({'regions': region_arr})


def get_hotels(request):
    """get hotels data from DB base on the user requested data

    Args:
        request (dict): [user requested data]

    Returns:
        [dict]: [hotel data]
    """
    hotel_arr = []
    hotels = None
    city_acronym = request.GET.get('city_acronym')
    region = request.GET.get('region')

    # filter hotels base on sended parameters
    if region == 'all':  # return all hotels of the selected city
        hotels = Hotel.objects.filter(city=city_acronym).values()
    else:
        # return hotels base on city and region
        hotels = Hotel.objects.filter(
            Q(city=city_acronym) & Q(region=region)).values()

    for h in hotels:
        hotel_arr.append(h)

    return JsonResponse({'hotels': hotel_arr})


# #  insert csv data in DB
# insert_csv = InsertCsv() # instantiate the insert class
# # call the insert city and hotel csv methods
# insert_csv.insert_city()
# insert_csv.insert_hotel()

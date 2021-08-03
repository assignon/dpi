from django.shortcuts import render
from django.db.models.query_utils import Q
# from models.user_model import User
import argparse
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
    return render(request, 'hotels/home.html')

from hotels.views import InsertCsv
import argparse
# from hotels.models import *



def main():
    parser = argparse.ArgumentParser(
        description='add city and hotel csv data to DB')

    parser.add_argument('-c', '--city', metavar='city',
                        required=False, help='city data')
    parser.add_argument('-ho', '--hotel', metavar='hotel',
                        required=False, help='hotel data')
    try:
        data = parser.parse_args()
        if data.city:
            print('city')
        else:
            print('hotel')
    except Exception:
        print('syntax not correct')


if __name__ == "__main__":
    main()



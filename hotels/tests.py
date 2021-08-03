from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from hotels.models import *
from hotels.views import home
import json
# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.region_url = reverse('region')
        self.hotel_url = reverse('hotel')
        self.home_url = reverse('home')

    def test_get_city_region_GET(self):
        response = self.client.get(self.region_url)

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'hotel')

    def test_get_hotels_GET(self):
        response = self.client.get(self.hotel_url)

        self.assertEqual(response.status_code, 200)

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotels/home.html')


class TestUrls(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))

        self.assertEqual(resolve(url).func, home)

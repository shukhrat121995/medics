from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import index, about, charts, details, getpersons


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_charts_url_is_resolved(self):
        url = reverse('charts')
        self.assertEqual(resolve(url).func, charts)

    def test_details_url_is_resolved(self):
        url = reverse('details', args=[1])
        self.assertEqual(resolve(url).func, details)

    def test_getpersons_url_is_resolved(self):
        url = reverse('getpersons')
        self.assertEqual(resolve(url).func, getpersons)
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.index_url = reverse('index')
        self.details_url = reverse('details', args=[1])
        self.about_url = reverse('about')
        self.charts_url = reverse('charts')

    def test_project_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/base.html')

    def test_project_details_GET(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/details.html')

    def test_project_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_project_charts_GET(self):
        response = self.client.get(self.charts_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/charts.html')



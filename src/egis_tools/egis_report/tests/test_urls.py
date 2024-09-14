from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve
from egis_report.views import Index, Report


class TestUrls(SimpleTestCase):

    def test_main_page_reverse(self):
        self.assertEqual(reverse("main"), "/")

    def test_main_page_resolve(self):
        self.assertIs(resolve("/").func.view_class, Index)
    
    def test_GET_main_page(self):
        client = Client()
        response = client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)     # successful

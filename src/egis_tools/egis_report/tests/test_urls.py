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
        self.assertEqual(response.status_code, 200)     # should be successful


    def test_report_page_reverse(self):
        self.assertEqual(reverse("report"), "/report/")

    def test_report_page_resolve(self):
        self.assertIs(resolve("/report/").func.view_class, Report)
    
    def test_GET_report_page(self):
        client = Client()
        response = client.get(reverse("report"))
        self.assertEqual(response.status_code, 400)     # should be bad request

    def test_GET_report_page_correct_parameter(self):
        client = Client()
        response = client.get(reverse("report") + "?amount=12")
        self.assertEqual(response.status_code, 200)


    def test_GET_report_page_incorrect_parameter_range(self):
        client = Client()
        response = client.get(reverse("report") + "?amount=-1")
        self.assertEqual(response.status_code, 400)

    def test_GET_report_page_incorrect_parameter_type(self):
        client = Client()
        response = client.get(reverse("report") + "?amount=asd")
        self.assertEqual(response.status_code, 400)

    def test_GET_report_page_incorrect_parameter_name(self):
        client = Client()
        response = client.get(reverse("report") + "?amoun=2")
        self.assertEqual(response.status_code, 400)

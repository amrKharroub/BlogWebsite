from django.urls import reverse
from django.test import TestCase


class TestHomeView(TestCase):
    def test_homepage_url(self):
        url = reverse("homepage")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_htmx(self):
        header = {"HTTP_HX_REQUEST": "true"}
        url = reverse("homepage")
        response = self.client.get(url, **header)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/components/list_elements.html")

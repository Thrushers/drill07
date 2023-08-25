from django.test import TestCase
from .models import *
from django.urls import reverse

# Create your tests here.
class LaboratorioTests(TestCase):

    @classmethod

    def setUpTestData(cls):

        cls.laboratorio = Laboratorio.objects.create(nombre='LaboratorioTest', ciudad='Ciudad Test', pais='País Test')

 

    def test_model_content(self):

        self.assertEqual(self.laboratorio.nombre, "LaboratorioTest")

        self.assertEqual(self.laboratorio.ciudad, "Ciudad Test")

        self.assertEqual(self.laboratorio.pais, "País Test")

 

    def test_url_exists_at_correct_location(self):

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

 

    def test_homepage(self):

        response = self.client.get(reverse("tabla"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "base.html")

        self.assertContains(response, "DRILL 07")
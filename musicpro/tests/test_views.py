from django.test import TestCase,Client
from django.urls import reverse
from apps.tienda.models import Product,Category,Marca
import json


# Prueba que la vista se asocia correctamente con la template
class Testviews(TestCase):

    def setUp(self):
        self.client = Client()
        self.products_url = reverse('store')
        
    def test_product_list_GET(self):

        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'store/store.html')

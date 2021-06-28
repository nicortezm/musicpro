from django.test import TestCase
from apps.tienda.models import Category,Product,Marca

class TestModels(TestCase):
    

    def setUp(self):
        self.marca1 = Marca.objects.create(
            marca_name ='Marca 1',
            description = 'Hola mundo' 
        )
        self.category = Category.objects.create(
            category_name = 'Categoria 1 ',
            slug = 'categoria-1'
        )
    def test_marca_is_created(self):
        desc_marca = 'Hola mundo'

        self.assertEqual(self.marca1.description,desc_marca)
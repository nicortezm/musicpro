from django.test import SimpleTestCase

from django.urls import reverse,resolve
from apps.tienda.views import store,product_detail


class TestUrls(SimpleTestCase):

    # Prueba del url llevando a una view
    def test_list_url_is_resolved(self):
        url = reverse('store')
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def test_category_url_is_resolved(self):
        url = reverse('products_by_category',args=['guitarras'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, store)

    def test_product_url_is_resolved(self):
        url = reverse('product_detail',args=['microfonos','microfono-condensador-samson-de-estudio-c01'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_detail)

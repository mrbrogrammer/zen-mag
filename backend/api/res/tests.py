from django.test import TestCase
from .models import Res


class ResModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Res.objects.create(title='first res')
        Res.objects.create(description='a description here')

    def test_title_content(self):
        res = Res.objects.get(id=1)
        expected_object_name = f'{res.title}'
        self.assertEquals(expected_object_name, 'first res')

    def test_description_content(self):
        todo = Res.objects.get(id=2)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')
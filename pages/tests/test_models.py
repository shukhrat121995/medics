from django.test import TestCase
from pages.models import Person


class TestModels(TestCase):
    def setUp(self) -> None:
        Person.objects.create(
            name='Shukhrat',
            gender='Male',
            place_of_birth='Tashkent',
        )

    def test_str_method(self):
        person = Person.objects.get(name='Shukhrat')
        self.assertEqual(person.__str__(), 'Shukhrat')

    def test_gender(self):
        person = Person.objects.get(name='Shukhrat')
        self.assertEqual(person.gender, 'Male')

    def test_place_of_birth(self):
        person = Person.objects.get(name='Shukhrat')
        self.assertEqual(person.place_of_birth, 'Tashkent')


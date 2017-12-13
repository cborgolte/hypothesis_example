from django.test import TestCase

# Create your tests here.
from hypothesis.extra.django import TestCase
from hypothesis import given, example, assume
from hypothesis.extra.django.models import models

from hypothesis.strategies import lists, just

from companies.models import Shop, Company


def generate_with_shops(company):
    return lists(models(Shop, company=just(company))).map(lambda _: company)


company_with_shops_strategy = models(Company).flatmap(generate_with_shops)


class TestProductTypeViewSet(TestCase):

    def setUp(self):
        self.url = "/insurance/v1/definitions/product-types/"

    @given(lists(company_with_shops_strategy))
    def test_1(self, companies):
        self.assertEqual(len(companies), Company.objects.count())

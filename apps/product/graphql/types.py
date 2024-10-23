from graphene_django import DjangoObjectType

from apps.product.models import Category, Brand, Color


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ColorType(DjangoObjectType):
    class Meta:
        model = Color
        fields = ['id', 'name']

import graphene

from apps.product.graphql.types import CategoryType, ColorType, BrandType
from apps.product.models import Category, Color, Brand


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    colors = graphene.List(ColorType)
    brands = graphene.List(BrandType)

    def resolve_categories(self, info):
        queryset = Category.objects.all()
        return queryset

    def resolve_colors(self, info):
        queryset = Color.objects.all()
        return queryset

    def resolve_brands(self, info):
        queryset = Brand.objects.all()
        return queryset

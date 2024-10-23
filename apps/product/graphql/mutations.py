import graphene

from apps.product.graphql.types import CategoryType, BrandType, ColorType
from apps.product.models import Category, Brand, Color


# -------------- Create --------------------
class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        category.save()
        return CreateCategory(category=category)


class CreateBrand(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    brand = graphene.Field(BrandType)

    def mutate(self, info, name):
        brand = Brand.objects.create(name=name)
        brand.save()
        return CreateBrand(brand=brand)


class CreateColor(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    colors = graphene.Field(ColorType)

    def mutate(self, info, name):
        colors = Category.objects.create(name=name)
        colors.save()
        return CreateCategory(colors=colors)


# --------------------- Delete -------------------------

class CategoryDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, id):
        category = Category.objects.filter(id=id)
        if category:
            category.delete()
            success = True
        else:
            success = False
        return CategoryDelete(success=success)


class ColorDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        color = Color.objects.filter(id=id)

        if color:
            color.delete()
            success = True
        else:
            success = False
        return ColorDelete(success=success)


class BrandDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        brand = Brand.objects.filter(id=id)

        if brand:
            brand.delete()
            success = True
        else:
            success = False
        return BrandDelete(success=success)


# ------------------------- Update ---------------------

class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    category = graphene.Field(CategoryType)  # -> yangilanga qiymatni category kaliti orqali koramniz

    def mutate(self, info, id, name=None):
        category = Category.objects.get(pk=id)
        if name:
            category.name = name
        category.save()
        return UpdateCategory(category=category)


class UpdateColor(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    color = graphene.Field(ColorType)  # -> yangilanga qiymatni color kaliti orqali koramniz

    def mutate(self, info, id, name=None):
        color = Color.objects.get(pk=id)
        if name:
            color.name = name
        color.save()
        return UpdateColor(color=color)


class UpdateBrand(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    brand = graphene.Field(BrandType)  # -> yangilanga qiymatni brand kaliti orqali koramniz

    def mutate(self, info, id, name=None):
        brand = Brand.objects.get(pk=id)
        if name:
            brand.name = name
        brand.save()
        return UpdateBrand(brand=brand)

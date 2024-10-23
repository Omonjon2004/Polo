import graphene

from apps.product.graphql.mutations import CreateCategory, CreateBrand, CreateColor, CategoryDelete, ColorDelete, \
    BrandDelete, UpdateColor, UpdateBrand, UpdateCategory
from apps.product.graphql.query import Query



class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_brand = CreateBrand.Field()
    create_color = CreateColor.Field()

    delete_category=CategoryDelete.Field()
    delete_color=ColorDelete.Field()
    delete_brand=BrandDelete.Field()

    update_color=UpdateColor.Field()
    update_brand=UpdateBrand.Field()
    update_category=UpdateCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

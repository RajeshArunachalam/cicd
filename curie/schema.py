import graphene
import coding.schema
import userapi.schema


class Query(coding.schema.Query, userapi.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    coding.schema.Mutation,
    userapi.schema.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
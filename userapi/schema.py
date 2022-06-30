import graphql_jwt
from django.db import models
from django.db.models import fields
import graphene
from graphene_django.types import DjangoObjectType
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

from .models import User, UserProfile


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    verify_token = graphql_jwt.Verify.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()


class User_schema(DjangoObjectType):
    class Meta:
        model = User
        fields = ("email", "is_staff")


class UserProfile_schema(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = ("user", "name")


class Query(UserQuery, MeQuery, graphene.ObjectType):
    user = graphene.List(User_schema)
    userprofile = graphene.List(UserProfile_schema)

    def resolve_user(root, info, **kwargs):
        # Querying a list
        return User.objects.all()

    def resolve_userprofile(root, info, *args, **kwargs):
        id = args.get("id")
        # Querying a list
        return UserProfile.objects.get(pk=id)


class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
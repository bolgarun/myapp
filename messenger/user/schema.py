import graphene
from graphene_django.types import DjangoObjectType
from user.models import AuthUser
from user.helpers import valid_password


class AuthUserType(DjangoObjectType):
	class Meta:
		model = AuthUser


class Query(graphene.AbstractType):
	users = graphene.List(AuthUserType, id=graphene.Int())

	def resolve_users(self, info, **kwargs):
		id = kwargs.get('id')
		if id is None:
			return AuthUser.objects.all()
		return AuthUser.objects.filter(pk=id)
	

class CreateUser(graphene.Mutation):
	class Input:
		username = graphene.String()
		password = graphene.String()
		created = graphene.DateTime()

	user = graphene.Field(AuthUserType)


	def mutate(self, info, username, password):
		user = AuthUser(username=username, password=password)
		if valid_password(user.password) != user.password:
			return ("Password and Confirm password need to be the same value")
		user.set_password(user.password)
		user.save()
		return CreateUser(user=user)


class Mutation(graphene.AbstractType):
	create_user = CreateUser.Field()
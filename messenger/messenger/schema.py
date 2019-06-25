import graphene
from  user.schema import Query as users_query
from  user.schema import Mutation as users_mutation

class Query(
	users_query,
	graphene.ObjectType):
	pass

class Mutation(users_mutation,
	graphene.ObjectType):
	pass
schema = graphene.Schema(query=Query, mutation=Mutation)	
import graphene
from graphene_django import DjangoObjectType
from api.models import ExternalUrls

class ExternalUrlObjectType(DjangoObjectType):
        class Meta:
            model = ExternalUrls
            fields = "__all__"
    
class ExternalUrlResolver:
    single_url = graphene.Field(ExternalUrlObjectType)
    all_urls = graphene.List(ExternalUrlObjectType)
    
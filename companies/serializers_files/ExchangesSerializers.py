from companies.default_imports import *

class ExchangesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companies_models.Exchanges
        fields = (
            'id',
            'name',
        )

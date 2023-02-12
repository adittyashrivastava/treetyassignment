from companies.default_imports import *

class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companies_models.Countries
        fields = (
            'id',
            'name',
        )

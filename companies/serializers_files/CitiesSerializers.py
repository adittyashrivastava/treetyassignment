from companies.default_imports import *
from companies import serializers_files

class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers_files.StatesSerializer()
    country = serializers_files.CountriesSerializer()

    class Meta:
        model = companies_models.Cities
        fields = (
            'id',
            'country',
            'state',
            'name',
        )

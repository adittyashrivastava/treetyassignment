from companies.default_imports import *
from companies import serializers_files

class StatesSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers_files.CountriesSerializer()

    class Meta:
        model = companies_models.States
        fields = (
            'id',
            'country',
            'name',
        )

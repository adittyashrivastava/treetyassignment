from companies.default_imports import *

class SectorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companies_models.Sectors
        fields = (
            'id',
            'name',
        )

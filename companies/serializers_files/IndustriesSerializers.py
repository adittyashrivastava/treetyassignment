from companies.default_imports import *
from companies import serializers_files

class IndustriesSerializer(serializers.HyperlinkedModelSerializer):
    related_sector = serializers_files.SectorsSerializer()

    class Meta:
        model = companies_models.Industries
        fields = (
            'id',
            'related_sector',
            'name',
        )

from companies.default_imports import *
from companies import serializers_files

class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    exchange = serializers_files.ExchangesSerializer()
    industry = serializers_files.IndustriesSerializer()
    city = serializers_files.CitiesSerializer()

    class Meta:
        model = companies_models.Companies
        fields = (
            'id',
            'exchange',
            'symbol',
            'shortname',
            'longname',
            'industry',
            'current_price',
            'marketcap',
            'ebitda',
            'revenue_growth',
            'city',
            'full_time_employees',
            'long_business_summary',
            'weight',
        )

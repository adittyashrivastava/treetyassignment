from rest_framework.views import APIView
from django.db import transaction
from companies.default_imports import companies_models, JsonResponse, serializers_files

class ListCountries(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.Countries.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'countries': serializers_files.CountriesSerializer(result, many=True).data
        })

class ListStates(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.States.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'states': serializers_files.StatesSerializer(result, many=True).data
        })

class ListCities(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.Cities.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'cities': serializers_files.CitiesSerializer(result, many=True, context={'request':request}).data
        })

class ListCompanies(APIView):

    def get(self, request, *args, **kwargs):
        page = int(kwargs['page']) #Pagination of 50 entries
        load_all = bool(kwargs['load_all'])

        all_companies_count = companies_models.Companies.objects.all().count()

        if page<1:
            return JsonResponse({
                'success': False,
                'error': 'page starts from 1',
                })

        if (page*50-all_companies_count)>=50:
            return JsonResponse({
                'success': True,
                'companies': [],
                })

        all_companies = companies_models.Companies.objects.all().order_by('-modified')[int((page-1)*50):int(page*50 if (page*50<=all_companies_count and not load_all) else all_companies_count)]

        return JsonResponse({
            'success': True,
            'companies': serializers_files.CompaniesSerializer(all_companies, many=True).data,
        })

class ListExchanges(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.Exchanges.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'exchanges': serializers_files.ExchangesSerializer(result, many=True).data
        })

class ListSectors(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.Sectors.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'sectors': serializers_files.SectorsSerializer(result, many=True).data
        })

class ListIndustries(APIView):

    def get(self, request, *args, **kwargs):
        result = companies_models.Industries.objects.all().order_by('name')

        return JsonResponse({
            'success': True,
            'industries': serializers_files.IndustriesSerializer(result, many=True).data
        })

# @transaction.atomic()
class AddCompany(APIView):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        company_info = request.data

        #Add if theres a new sector
        if type(company_info.get("sector"))==str:
            sector_obj, _ = companies_models.Sectors.objects.get_or_create(
                name = company_info.get("sector").title()
            )

            sector_id = sector_obj.id
        else:
            if company_info.get("sector")!=0:
                sector_id = company_info.get("sector")
            else:
                sector_id = None

        #Add info if theres a new industry
        if type(company_info.get("industry"))==str:
            industry_obj, _ = companies_models.Industries.objects.get_or_create(
                related_sector_id = sector_id,
                name = company_info.get("industry").title()
            )

            industry_id = industry_obj.id

        else:
            if company_info.get("industry")!=0:
                industry_id = company_info.get("industry")
                industry_obj = companies_models.Industries.objects.get(id = industry_id)
            else:
                industry_id = None
                industry_obj = None

        if industry_obj!=None:
            if industry_obj.related_sector_id==None:
                industry_obj.related_sector_id = sector_id
                industry_obj.save()

        #Add if theres a new exchange
        if type(company_info.get("exchange"))==str:
            exchange_obj, _ = companies_models.Exchanges.objects.get_or_create(
                name = company_info.get("exchange").upper()
            )

            exchange_id = exchange_obj.id

        else:
            if company_info.get("exchange")!=0:
                exchange_id = company_info.get("exchange")
                exchange_obj = companies_models.Exchanges.objects.get(id = exchange_id)
            else:
                exchange_id = None
                exchange_obj = None

        #Add if theres a new country
        if type(company_info.get("country"))==str:
            country_obj, _ = companies_models.Countries.objects.get_or_create(
                name = company_info.get("country").capitalize()
            )

            country_id = country_obj.id

        else:
            if company_info.get("country")!=0:
                country_id = company_info.get("country")
                country_obj = companies_models.Countries.objects.get(id = country_id)
            else:
                country_id = None
                country_obj = None

        #Add if theres a new state
        if type(company_info.get("state"))==str:
            state_obj, _ = companies_models.States.objects.get_or_create(
                country_id = country_id,
                name = company_info.get("state").capitalize()
            )

            state_id = state_obj.id

        else:
            if company_info.get("state"):
                state_id = company_info.get("state")
                state_obj = companies_models.States.objects.get(id = state_id)
            else:
                state_id = None
                state_obj = None

        if state_obj!=None:
            if state_obj.country_id==None:
                state_obj.country_id = country_id
                state_obj.save()

        #Add if theres a new city
        if type(company_info.get("city"))==str:
            city_obj, _ = companies_models.Cities.objects.get_or_create(
                country_id = country_id,
                state_id = state_id,
                name = company_info.get("city").capitalize()
            )

            city_id = city_obj.id

        else:
            if company_info.get("city"):
                city_id = company_info.get("city")
                city_obj = companies_models.Cities.objects.get(id = city_id)
            else:
                city_id = None
                city_obj = None

        if city_obj!=None:
            if city_obj.state_id==None:
                city_obj.state_id = state_id
                city_obj.save()

            if city_obj.country_id==None:
                city_obj.country_id = country_id
                city_obj.save()

        company_obj = companies_models.Companies.objects.create(
            exchange_id = exchange_id,
            symbol = company_info.get("symbol").upper(),
            shortname = company_info.get("shortname").title(),
            longname = company_info.get("longname").title(),
            industry_id = industry_id,
            current_price = company_info.get("current_price"),
            marketcap = company_info.get("marketcap"),
            ebitda = company_info.get("ebitda"),
            revenue_growth = company_info.get("revenue_growth"),
            city_id = city_id,
            full_time_employees = company_info.get("full_time_employees"),
            long_business_summary = company_info.get("long_business_summary").capitalize() if company_info.get("long_business_summary")!=None else None,
            weight = company_info.get("weight"),
        )

        return JsonResponse({
            'success': True,
            'added_company': serializers_files.CompaniesSerializer(company_obj).data
        })

from django.urls import path
from .views import *

urlpatterns = [
    path("list-countries/", ListCountries.as_view(), name="list_countries"),
    path("list-states/", ListStates.as_view(), name="list_states"),
    path("list-cities/", ListCities.as_view(), name="list_cities"),
    path("list-companies/<int:page>/<int:load_all>/", ListCompanies.as_view(), name="list_companies"),
    path("add-company/", AddCompany.as_view(), name="add_company"),
    path("list-exchanges/", ListExchanges.as_view(), name="list_exchanges"),
    path("list-sectors/", ListSectors.as_view(), name="list_sectors"),
    path("list-industries/", ListIndustries.as_view(), name="list_industries"),
]
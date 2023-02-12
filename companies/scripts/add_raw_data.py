import pandas as pd
from pathlib import Path
import companies.models as companies_models


def inject_data():
    path_dir = Path(__file__).resolve().parent / "sp500_companies.csv"
    raw_data = pd.read_csv(path_dir)

    for i in range(raw_data.shape[0]):
        temp = raw_data.iloc[i]

        try:
            exchange_id = companies_models.Exchanges.objects.get(
                name__iexact = temp['Exchange']
            ).id

        except companies_models.Exchanges.DoesNotExist:
            exchange_obj = companies_models.Exchanges.objects.create(
                name = temp['Exchange']
            )

            exchange_id = exchange_obj.id

        try:
            sector_id = companies_models.Sectors.objects.get(
                name__iexact = temp['Sector']
            ).id

        except companies_models.Sectors.DoesNotExist:
            sector_obj = companies_models.Sectors.objects.create(
                name = temp['Sector']
            )

            sector_id = sector_obj.id

        try:
            industry_id = companies_models.Industries.objects.get(
                related_sector_id = sector_id,
                name__iexact = temp['Industry']
            ).id

        except companies_models.Industries.DoesNotExist:
            industry_obj = companies_models.Industries.objects.create(
                related_sector_id = sector_id,
                name = temp['Industry']
            )

            industry_id = industry_obj.id

        try:
            country_id = companies_models.Countries.objects.get(
                name__iexact = temp['Country']
            ).id

        except companies_models.Countries.DoesNotExist:
            country_obj = companies_models.Countries.objects.create(
                name = temp['Country']
            )

            country_id = country_obj.id

        if not pd.isna(temp['State']):
            try:
                state_id = companies_models.States.objects.get(
                    country_id = country_id,
                    name__iexact = temp['State']
                ).id

            except companies_models.States.DoesNotExist:
                state_obj = companies_models.States.objects.create(
                    country_id = country_id,
                    name = temp['State']
                )

                state_id = state_obj.id

        else:
            state_id=None

        try:
            city_id = companies_models.Cities.objects.get(
                name__iexact = temp['City']
            ).id

        except companies_models.Cities.DoesNotExist:
            city_obj = companies_models.Cities.objects.create(
                country_id = country_id,
                state_id = state_id,
                name = temp['City']
            )

            city_id = city_obj.id

        company_obj = companies_models.Companies.objects.create(
            exchange_id = exchange_id,
            symbol = temp['Symbol'],
            shortname = temp['Shortname'],
            longname = temp['Longname'],
            industry_id = industry_id,
            current_price =  None if pd.isna(temp['Currentprice']) else temp['Currentprice'],
            marketcap = None if pd.isna(temp['Marketcap']) else temp['Marketcap'],
            ebitda =  None if pd.isna(temp['Ebitda']) else temp['Ebitda'],
            revenue_growth = None if pd.isna(temp['Revenuegrowth']) else temp['Revenuegrowth'],
            city_id = city_id,
            full_time_employees = None if pd.isna(temp['Fulltimeemployees']) else temp['Fulltimeemployees'],
            long_business_summary = None if pd.isna(temp['Longbusinesssummary']) else temp['Longbusinesssummary'],
            weight = None if pd.isna(temp['Weight']) else temp['Weight'],
        )

    return

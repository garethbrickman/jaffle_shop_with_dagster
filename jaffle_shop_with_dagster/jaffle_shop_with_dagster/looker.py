from .assets import jaffle_shop_dbt_assets

from dagster import asset
from dagster_dbt import get_asset_key_for_model

@asset(deps=get_asset_key_for_model([jaffle_shop_dbt_assets], "raw_customers"))
def bigquery_view():
    return "bigquery_view"
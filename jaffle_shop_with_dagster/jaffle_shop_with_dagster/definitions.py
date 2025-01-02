from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import jaffle_shop_dbt_assets
from .project import jaffle_shop_project
from .schedules import schedules
from .looker import bigquery_view

defs = Definitions(
    assets=[jaffle_shop_dbt_assets, bigquery_view],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=jaffle_shop_project),
    },
)

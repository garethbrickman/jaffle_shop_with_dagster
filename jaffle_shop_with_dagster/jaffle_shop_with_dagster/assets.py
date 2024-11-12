from dagster import AssetExecutionContext, AssetKey
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator
from typing import Any, Mapping

from .project import jaffle_shop_project


@dbt_assets(manifest=jaffle_shop_project.manifest_path)
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    dbt_command = [
        "run",
        "--log-format", "json"
    ]
    yield from dbt.cli(dbt_command, context=context).stream()

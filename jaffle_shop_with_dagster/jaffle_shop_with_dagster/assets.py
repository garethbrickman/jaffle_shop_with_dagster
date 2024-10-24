from dagster import AssetExecutionContext, AssetKey
from dagster_dbt import DbtCliResource, dbt_assets, DagsterDbtTranslator
from typing import Any, Mapping

from .project import jaffle_shop_project


# @dbt_assets(manifest=jaffle_shop_project.manifest_path)
# def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
#     yield from dbt.cli(["build"], context=context).stream()

class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props: Mapping[str, Any]) -> AssetKey:
        return super().get_asset_key(dbt_resource_props).with_prefix("code_location_2")

@dbt_assets(
    manifest=jaffle_shop_project.manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator(),
)
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

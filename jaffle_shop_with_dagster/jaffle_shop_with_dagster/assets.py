from dagster import AssetExecutionContext, Config, asset
from dagster_dbt import DbtCliResource, dbt_assets, get_asset_key_for_model


from .project import jaffle_shop_project

dbt = DbtCliResource(
    project_dir=jaffle_shop_project.project_dir,
)

@dbt_assets(manifest=jaffle_shop_project.manifest_path)
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    dbt_build_args = ["build"]

    yield from dbt.cli(dbt_build_args, context=context).stream()

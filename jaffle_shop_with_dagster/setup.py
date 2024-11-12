from setuptools import find_packages, setup

DAGSTER_VERSION = "1.9.0"
DAGSTER_LIBRARY_VERSION = "0.25." + DAGSTER_VERSION.split(".")[2]

setup(
    name="jaffle_shop_with_dagster",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "jaffle_shop_with_dagster": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        f"dagster=={DAGSTER_VERSION}",
        f"dagster-cloud=={DAGSTER_VERSION}",
        f"dagster-dbt=={DAGSTER_LIBRARY_VERSION}",
        f"dbt-duckdb<1.9",
    ],
    extras_require={
        "dev": [
            f"dagster-webserver=={DAGSTER_VERSION}",
        ]
    },
)

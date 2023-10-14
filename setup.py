from setuptools import setup, find_packages

setup(
    name="ETLQueryTool",
    version="0.1.0",
    description="ETL-Query tool for data processing",
    author="Yabei Zeng",
    packages=find_packages(),
    install_requires=[
        "black==22.3.0",
        "click==8.1.3",
        "pytest==7.1.3",
        "pytest-cov==4.0.0",
        "requests==2.26.0",
        "ruff==0.0.284",
        "pandas",
        "python-dotenv",
        "databricks-sql-connector",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)

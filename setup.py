from setuptools import setup, find_packages

setup(
    name="ETLQueryTool",
    version="0.1.0",
    description="ETL-Query tool for data processing",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)

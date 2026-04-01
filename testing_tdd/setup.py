from setuptools import (
    setup, 
    find_packages
)

setup(
    name = "ndfl",
    version = "0.0.1",
    long_description = "Tax calculator",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src")
)


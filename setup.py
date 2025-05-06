from setuptools import setup, find_packages

with open("version.txt") as f:
    version = f.read().strip()

setup(
    name="lib-version",
    version=version,
    packages=find_packages(),
    include_package_data=True,
)

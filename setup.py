from setuptools import setup, find_packages

setup(
    name="lib_version",
    version="1.0.9",  # Or keep reading from the file if preferred
    packages=find_packages(),
    include_package_data=True,
    package_data={"lib_version": ["version.txt"]},  # ✅ include the version file
)

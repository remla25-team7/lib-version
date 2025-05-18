from setuptools import setup, find_packages

setup(
    name="libversion",
    version="1.0.8",  # Or keep reading from the file if preferred
    packages=find_packages(),
    include_package_data=True,
    package_data={"libversion": ["version.txt"]},  # ✅ include the version file
)

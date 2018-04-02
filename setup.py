from setuptools import find_packages, setup

setup(
    name="samur",
    version="0.1.0",
    author="Caner Durmusoglu",
    author_email="cnr437@gmail.com",
    include_package_data=True,
    packages=find_packages(),
    url="",
    # license="LICENSE.txt",
    description="Samur MainBoard Python Module",
    # long_description=open("README.md").read(),
    # Dependent packages (distributions)
    install_requires=[
        "RPi.GPIO",
    ],
)
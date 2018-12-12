from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='internal_aireldentalchairs_com',
    version=version,
    description='AirelDentalChairs.com website',
    author='Frappe',
    author_email='web@uandh.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)

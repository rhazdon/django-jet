import os

from setuptools import setup, find_packages


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding="utf-8")
    except TypeError:
        file = open(path)
    return file.read()


def get_install_requires():
    return ["Django", "django-admin-rangefilter"]


setup(
    name="django-jet",
    version=__import__("jet").VERSION,
    description="Modern template for Django admin interface with improved functionality",
    long_description=read("README.rst"),
    author="Denis Kildishev",
    author_email="support@jet.geex-arts.com",
    url="https://github.com/geex-arts/django-jet",
    packages=find_packages(),
    license="AGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "License :: Free for non-commercial use",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Web Environment",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces",
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=get_install_requires(),
)

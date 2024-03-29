import os

from setuptools import find_packages, setup


setup(
    name="django-evade",
    version="0.2.3",
    description="A Django template filter to convert HTML literals into named, decimal, or hexadecimal forms",
    long_description=open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.rst")
    ).read(),
    long_description_content_type="text/x-rst",
    author="Richard Cornish",
    author_email="rich@richardcornish.com",
    url="https://github.com/richardcornish/django-evade",
    license="BSD",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.6",
    install_requires=["Django>=3.2"],
)

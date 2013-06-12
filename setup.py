#!/usr/bin/env python
from setuptools import setup


setup(
    name="django-crowd-rest-backend",
    version=":versiontools:crowdrest:__version__",
    description="Django authentication backend for Atlassian Crowd REST API with groups support.",
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    zip_safe=True,
    packages=['crowdrest'],
    # dependencies
    install_requires=['django >= 1.3'],
    setup_requires=['versiontools >= 1.3.1'],
)

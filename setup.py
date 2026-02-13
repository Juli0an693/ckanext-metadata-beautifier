# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='ckanext-metadata-beautifier',
    version='0.1',
    entry_points={
        'ckan.plugins': [
            'metadata-beautifier=ckanext.metadata_beautifier.plugin:MetadataBeautifierPlugin',
        ],
        'babel.extractors': [
            'ckan = ckan.lib.extract:extract_ckan',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    message_extractors={
        "ckanext": [
            ("**.py", "python", None),
            ("**/templates/**.html", "ckan", None),
            ("**/public/**", "ignore", None),
        ],
    }
)
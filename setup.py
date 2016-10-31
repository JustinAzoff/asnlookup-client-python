from setuptools import setup, find_packages

version = '0.0.3'
long_description = ""

setup(name='asnlookup-client',
      version=version,
      description="ASN Lookup Client",
      long_description=long_description,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ASN',
      author='Justin Azoff',
      author_email='justin@bouncybouncy.net',
      url='',
      license='MIT',
      py_modules=['asnlookup_client'],
      include_package_data=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "pyzmq",
      ],
      entry_points = {
        'console_scripts': [
            'asnlookup-client   = asnlookup_client:main',
        ]
      },
  )

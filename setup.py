from setuptools import find_packages, setup

setup(
  name='mlops',
  version='0.1.0',
  packages=find_packages(),
  description='MLOps Sample',
  author='Avinash Manure',
  license='MIT',
  entrypoints={
    'console_scripts': [
      'classification=src.main:main',
    ],
  },
)
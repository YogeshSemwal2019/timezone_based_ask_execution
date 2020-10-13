# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='timezone_based_ask_execution',
    version='0.1.0',
    description='Timezone based Task Execution',
    long_description=readme,
    author='Yogesh Semwal',
    author_email='yogeshsemwal403@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
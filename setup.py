# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

requirements = open('requirements.txt').read().splitlines()
long_description = open('README.txt').read()

setup(
    name='pychords',
    version='0.0.1a',
    description='Python guitar natural chords',
    author='Jesus Galan',
    author_email='jgc.developments@outlook.com',
    license='MIT',
    packages=find_packages(exclude=['specs', 'specs.*']),
    install_requires=requirements,
)

# setup.py
from setuptools import setup, find_packages

setup(
    name='Django_GCC_PhoneNumbers',
    version='0.0.1',  
    description='A flexible and extensible phone number validation package for GCC countries and Egypt.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Moataz Fawzy',
    author_email='motazfawzy73@gmail.com',
    url='https://github.com/Moataz0000/Django-Phone-Number-Field-GCC',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
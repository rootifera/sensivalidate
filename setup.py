from setuptools import setup, find_packages

setup(
    name="sensivalidate",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'creditcard==1.0.2',
    ],
    description="A module to find credit card, UK bank account, sort code and postcode in text",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Omur Ozbahceliler",
    author_email="omur@rootifera.org",
    url="https://github.com/rootifera/sensivalidate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


from setuptools import setup
from setuptools import find_packages

setup(
    name='my_package',
    version='1.0.0',
    description="Python DS Lab Assignment",
    packages=find_packages(),
    author='Kaushal Kumar',
    author_email='kaushalkumarsingh2026@gmail.com',
    install_requires=[
        'numpy == 1.21.5',
        'opencv-python-headless',
        'Pillow == 9.4.0',
        'spacy',
        'torchvision',
        'jsonlines == 3.1.0',
        'pillow',
        'requests',
        'en_core_web_sm',
        'torch',
        'salesforce-lavis'
    ]
)
import setuptools
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import sys
import os

setup(
    name="multimodal_calibration",
    version="0.0.1",
    description="A package for the calibration of multiple sensors",
    author="bernardomig",
    author_email="bernardo.lourenco@ua.pt",
    packages=
        find_packages(),
    install_requires=[
        'numpy >= 1.16.5', 
        'opencv-python >= 4.1.0.25'],
)

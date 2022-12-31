# ==============================================================================
# Name:     setup.py
# Author:   Bloom, Matthew 
# Created:  12/31/2022
# Modified: 12/31/2022
#
# ==============================================================================
# Description
# ------------------------------------------------------------------------------
# Setup file for pennywise.
#
# ==============================================================================
# History
# ------------------------------------------------------------------------------
# Revision on https://github.com/mbloom88/pennywise.
#
# ==============================================================================

# ==============================================================================
# PACKAGES
# ==============================================================================

from setuptools import setup, find_packages

# ==============================================================================
# SETUP
# ==============================================================================

setup(
    name="pennywise",
    version="0.1.0",
    author="Matthew Bloom",
    author_email="matthewabloom88@gmail.com",
    description="A personal budgeting application.",
    url="https://github.com/mbloom88/pennywise",
    packages=find_packages(include=['pennywise', 'pennywise.*']),
    install_requires=[
        'PyQt5==5.15.7',
        'PyQt5Designer==5.14.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.1'
)

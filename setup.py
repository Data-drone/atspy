from setuptools import setup, Command
import os
import sys



setup(name='atspy',
      version='0.2.6-dev',
      description='Automated Time Series in Python',
      url='https://github.com/firmai/atspy',
      author='snowde',
      author_email='d.snow@firmai.org',
      license='MIT',
      packages=['atspy'],
      install_requires=[

            "cachetools",
            "Cython",
            "dataclasses",
            "DateTime",
            "decorator",
            "easydict",
            "prophet",
            "gluonts",
            "gunicorn",
            "lightgbm",
            "matplotlib",
            "mxnet",
            "numba",
            "numexpr",
            "pandas",
            "pip-tools",
            "pmdarima",
            "psutil",
            "scikit-learn",
            "scipy",
            "seaborn",
            "sklearn",
            "statsmodels",
            "sympy",
            "tbats",
            "tblib",
            "tensorflow",
            "tflearn",
            "torch",
            "tqdm",
            "tsfresh",
            "tweepy",
            "typing",
            "typing-extensions",
            "xlrd",
            "seasonal",
            "nbeats-pytorch",
            "gluonts",
            "numpy",
            "pydantic"
            ],
            
      zip_safe=False)

from setuptools import setup, find_packages

setup(
    name='correlations',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    python_requires='>=3.6.*',
    install_requires=[
    ]
)

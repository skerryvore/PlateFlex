import setuptools
from numpy.distutils.core import setup, Extension

ext = [Extension(name='plateflex.cpwt',
                sources=['src/cpwt.f90', 'src/cpwt_sub.f90'])]

setup(
    name                = 'plateflex',
    version             = '0.0.1',
    description         = 'Python package for estimating lithospheric elastic thickness',
    author              = 'Pascal Audet',
    maintainer          = 'Pascal Audet',
    author_email        = 'pascal.audet@uottawa.ca',
    url                 = 'https://github.com/paudetseis/PlateFlex', 
    # download_url        = 'https://github.com/paudetseis/Telewavesim/archive/0.1.0.tar.gz',
    classifiers         = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'],
    install_requires    = ['numpy>=1.15', 'matplotlib'],
    python_requires     = '>=3.5',
    tests_require       = ['pytest'],
    ext_modules         = ext,
    packages            = ['plateflex'],
    package_data        = {
        'plateflex': [
            # 'examples/*.ipynb',
            'examples/data/*.txt',
            'examples/Notebooks/*.py']
    }
)
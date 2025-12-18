# Minimal setup.py for Cython extensions only
from setuptools import setup
from distutils.extension import Extension

USE_CYTHON = False
try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    pass

ext = 'pyx' if USE_CYTHON else 'c'
extensions = [
    Extension('hichiarep.util', [f'hichiarep/util.{ext}']),
]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions, language_level=3)

setup(ext_modules=extensions)
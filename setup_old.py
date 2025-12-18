import setuptools
from distutils.extension import Extension

USE_CYTHON = False
try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    pass

ext = 'pyx' if USE_CYTHON else 'c'
extensions = [
    Extension('hichiarep.util',
              [f'hichiarep/util.{ext}']),
]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions, language_level=3)

NAME = 'HiChIA-Rep'

setuptools.setup(

    name=NAME,

    use_scm_version=True,

    setup_requires=['setuptools_scm'],

    author="Sion Kim",

    author_email="sionkim@umich.edu",

    description="A package for quantifying the similarity between chromatin interactions data enriched for protein binding sites or open chromatin regions",

    long_description=open('README.md').read(),

    long_description_content_type="text/markdown",

    url="https://github.com/minjikimlab/hichiarep",

    packages=['hichiarep'],

    include_package_data=True,

    install_requires=[
        'numpy>=2.2,<2.3',
        'scipy>=1.15,<1.16',
        'matplotlib>=3.10,<3.11',
        'click',
        'pybedgraph>=0.5',
        'pybedtools>=0.12',
        'hic-straw==1.3',
    ],

    python_requires='>=3.10',

    ext_modules=extensions,

    license="MIT",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)

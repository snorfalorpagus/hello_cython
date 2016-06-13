from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import sys

compiler_directives = {}
define_macros = []

compiler_directives['profile'] = True
compiler_directives['linetrace'] = True
define_macros.append(('CYTHON_TRACE', '1'))


extensions = [
    Extension("hello", ["hello.pyx"],
        include_dirs=[],
        libraries=[],
        library_dirs=[],
        define_macros=define_macros,
        )
]

setup(
    name = "Hello",
    ext_modules = cythonize(extensions, compiler_directives=compiler_directives),
)

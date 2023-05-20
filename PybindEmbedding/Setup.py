from setuptools import setup, Extension
import pybind11

sfc_module = Extension(
    'ComponentModel',
    sources=['wComponent.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7'],
    )

setup(
    name='ComponentModel',
    version='1.0',
    description='Python package with testin components message interaction through C++ extension (PyBind11)',
    ext_modules=[sfc_module],
)
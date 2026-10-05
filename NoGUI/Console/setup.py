print("start")

from distutils.core import setup
from Cython.Build import cythonize

print("start2")
setup(name = "main_pyd",ext_modules = cythonize("main.py"))
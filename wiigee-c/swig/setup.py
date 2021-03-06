#!/usr/bin/env python

#!/usr/bin/env python

"""
setup.py file for SWIG hmm
"""

from distutils.core import setup, Extension


quantizer_module = Extension('_quantizer',
                           include_dirs=['../include/', ],
                           sources=['quantizer_wrap.c', '../lib/quantizer.c','../lib/util.c'],
                           extra_compile_args=["-std=c99",],
                           )

setup (name = 'hmm',
       version = '0.1',
       author      = "Noisebridge Machine Learning",
       description = """Implements kmeans clustering""",
       ext_modules = [quantizer_module],
       py_modules = ["quantizer"],
       )


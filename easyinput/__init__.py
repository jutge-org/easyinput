"""
easyinput package
https://github.com/jutge-org/easy-input
"""

from easyinput.tokenizer import *

# current version
version = "2.3"

# Specify what to import with *:
__all__ = [
    'read',
    'read_many',
    'read_line',
    'read_many_lines',
    'set_eof_handling',
    'EOFModes',
]

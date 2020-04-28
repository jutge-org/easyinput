"""
jutge package for alternative input handling.
see https://github.com/jutge-org/jutge-python
"""

from jutge.reader.tokenizer import *

version = "2.2"  # current version

# Specify what to import with *:
__all__ = [
    'read', 'read_many',
    'read_line', 'read_many_lines',
    'set_eof_handling', 'EOFModes'
]

"""import_parent_dir - """

__version__ = '0.1.0'
__author__ = 'fx-kirin <fx.kirin@gmail.com>'
__all__ = []

import os
import sys
import inspect


def import_parent(count=1):
    caller_file_path = os.path.abspath(inspect.stack()[1].filename)
    import_file_path = os.path.dirname(caller_file_path)
    for _ in range(count):
        import_file_path = os.path.dirname(import_file_path)

    if import_file_path not in sys.path:
        sys.path.append(import_file_path)

"""add_parent_path - """

__version__ = '0.1.2'
__author__ = 'fx-kirin <fx.kirin@gmail.com>'
__all__ = []

import os
import sys
import inspect


def add_parent_path(count=1):
    caller_file_path = os.path.abspath(inspect.stack()[1].filename)
    import_file_path = os.path.dirname(caller_file_path)
    for _ in range(count):
        import_file_path = os.path.dirname(import_file_path)

    if import_file_path not in sys.path:
        sys.path.append(import_file_path)
        return AddParentPath(import_file_path)
    else:
        return AddParentPath()


class AddParentPath(object):
    def __init__(self, import_file_path):
        self.import_file_path = import_file_path

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, trace):
        if self.import_file_path in sys.path:
            sys.path.remove(self.import_file_path)

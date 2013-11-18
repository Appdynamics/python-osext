#coding: utf-8

from os import chdir, getcwd
from os.path import realpath, isdir


class PushdContext:
    cwd = None
    original_dir = None

    def __init__(self, dirname):
        self.cwd = realpath(dirname)

    def __enter__(self):
        self.original_dir = getcwd()
        chdir(self.cwd)
        return self

    def __exit__(self, type, value, tb):
        chdir(self.original_dir)


def pushd(dirname):
    return PushdContext(dirname)

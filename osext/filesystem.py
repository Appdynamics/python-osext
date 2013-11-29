# coding: utf-8

from os.path import join as path_join, getmtime
from sh import rsync
import os
import subprocess as sp


def isfile(filename, mode='rb'):
    try:
        with open(filename, mode):
            return True
    except IOError:
        pass

    return False


def rm_files(files_list, raise_on_error=False):
    for filename in files_list:
        try:
            os.remove(filename)
        except OSError as e:
            if raise_on_error:
                raise e


def sync(remote_dir, target_dir):
    if '/' not in remote_dir[-1]:
        remote_dir += '/'

    output = rsync('-a', remote_dir, target_dir)

    return output.exit_code


def has_same_time(filename, filetime):
    return getmtime(filename) == filetime

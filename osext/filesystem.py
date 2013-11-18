# coding: utf-8

from os.path import join as path_join, getmtime
import os
import subprocess as sp


def isfile(filename, mode='rb'):
    try:
        with open(filename, mode):
            return True
    except IOError:
        pass

    return False


def rmdir_force(dir_name):
    return sp.check_call(['rm', '-fR', dir_name])


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

    return sp.check_call(['rsync', '-a', remote_dir, target_dir])


def has_same_time(filename, filetime):
    return getmtime(filename) == filetime

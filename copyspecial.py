#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Michael Trepanier"

# import re
import sys
import shutil
# import subprocess
import argparse
import os
# from zipfile import ZipFile
# from os import listdir


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""

    special_files = []
    dirname = os.path.abspath(dirname)
    file_list = os.listdir(dirname)
    for file in file_list:
        parts = file.split('__')
        if (len(parts) >= 3):

            special_files.append(dirname+'/'+file)

    # print(special_files)
    return special_files


def copy_to(path_list, dest_dir):
    """This copies to a new directory"""

    os.makedirs(dest_dir, exist_ok=True)
    if not os.path.isdir(dest_dir):
        print(f"{dest_dir} is NOT a directory")
        sys.exit(1)
    for f in path_list:
        shutil.copy(f, dest_dir)


def zip_to(path_list, dest_zip):
    """This zips files with the destination directory"""
    cmd_str = 'zip -j '+dest_zip
    for file in path_list:
        cmd_str = cmd_str+' '+file

    # print('Command I am going to do:')
    print(cmd_str)
    # os.system(cmd_str)
    stream = os.popen(cmd_str)
    output = stream.read()
    # subprocess.run(cmd_str)

    print(output)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dirs', help='directory(s) to search')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # print(ns)

    if ns.dirs is not None:

        special_paths = get_special_paths(ns.dirs)
        print("\n".join(special_paths))
    if ns.todir is not None:
        copy_to(special_paths, ns.todir)

    if ns.tozip is not None:
        zip_to(special_paths, ns.tozip)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])

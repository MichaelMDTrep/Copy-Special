#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Michael Trepanier"

import re
import sys
import shutil
import subprocess
import argparse
import os.path
# from os import listdir


def get_special_paths(dirs):
    """Given a dirname, returns a list of all its special files."""

    special_files = []
    print(dirs)
    for dirname in dirs:
        file_list = os.listdir(dirname)
        # print(file_list)
        for file in file_list:
            # print(file)
            parts = file.split('__')
            # print(parts)
            if (len(parts) >= 3):
                print(file)
                if (file in special_files):
                    print(file+" is a duplicate")
                    sys.exit(1)
                else:
                    special_files.append(file)

    print(special_files)
    return special_files


def copy_to(path_list, dest_dir):

    path_list = os.listdir("/home/")
    dest_dir = "/home/mtrepanier935/kenzie-q3/Copy-Special"
    for files in path_list:
        if files.endswith(".txt"):
            shutil.copy(path_list, dest_dir)

###########
    shutil.copyfile(path_list, dest_dir)
    print(path_list)

    return


def zip_to(path_list, dest_zip):

    print(f"Command i'm going to do: \nzip -j {dest_zip}")

    command_list = ['zip', '-j', dest_zip]
    subprocess.run(
        command_list,
    )
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dirs', help='directory(s) to search', nargs='+')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    print(ns)

    if (ns.dirs != None):
        get_special_paths(ns.dirs)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])

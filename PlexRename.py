#!/usr/bin/python3

import glob
import os
import sys
import re


def find_needed_parts(filename):
    ep_reg = re.search("(E|e)(\d+)", filename)
    if ep_reg:
        found_ep = ep_reg.group(2)
    s_reg = re.search("(S|s)(\d+)", filename)
    if s_reg:
        found_s = s_reg.group(2)
    ext_reg = re.search("\.(\w+)", filename)
    if ext_reg:
        ext = ext_reg.group(1)
    body_reg = re.search("((^(.*?)([^E0-9])+)|(^(.*?)([^e0-9])))", filename)
    if body_reg:
        body = body_reg.group(1)
    return body, found_ep, found_s, ext


def main():
    if len(sys.argv) != 3:
        print("Enter file as first argument and directory as second")
        exit(3)
    filename = sys.argv[1]
    directory = sys.argv[2]
    body, ep, s, ext = find_needed_parts(filename)
    file_rename_pattern = "*." + ext

    for pathAndFilename in glob.iglob(os.path.join(directory, file_rename_pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        ep = int(ep) + 1  # type: int
        rename_name = str(body + 'S' + s + 'E' + str(ep) + ext)
        os.rename(pathAndFilename, os.path.join(directory, rename_name))


main()

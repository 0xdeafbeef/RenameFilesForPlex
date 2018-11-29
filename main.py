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
    filename = sys.argv[1]
    direct = sys.argv[2]
    print(filename)
    print(direct)
    body, ep, s, ext = find_needed_parts(filename)
    pattern = "*." + ext

    for pathAndFilename in glob.iglob(os.path.join(direct, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        ep = int(ep) + 1  # type: int
        rename_name = str(body + 'S' + s + 'E' + str(ep) + '.' + ext)
        os.rename(pathAndFilename, os.path.join(direct, rename_name))


main()

#!/usr/bin/python3

import glob
import os
import sys
import re


def find_needed_parts(filename):
    ext_reg = re.search("\.(\w+)", filename)
    if ext_reg:
        ext = ext_reg.group(1)
    return ext


def main():
    if len(sys.argv) != 2:
        print("Enter file as first argument and directory as second")
        exit(3)
    print("How name of your show looks? If like ShowName EpisodeNumber SeasonNumber enter 1\n "
          "If like ShowName SeasonNumber EpisodeNumber enter 2")
    filetype = int(input("Enter 1 or 2: \n"))
    filename = sys.argv[1]
    if filetype == 1:
        p = re.search("^.+S\d+", filename)
        if p:
            body = p.group(0)

    ext = find_needed_parts(filename)
    file_rename_pattern = "*." + ext

    for pathAndFilename in glob.iglob(file_rename_pattern):
        p = re.search("^.+S\d+", pathAndFilename)
        if p:
            body = p.group(0)
        body = body + '.' + ext
        os.rename(pathAndFilename, body)


main()

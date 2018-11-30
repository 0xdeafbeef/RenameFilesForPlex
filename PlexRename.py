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

    ext = find_needed_parts(filename)
    file_rename_pattern = "*." + ext

    for pathAndFilename in glob.iglob(file_rename_pattern):
        body = None
        if filetype == 1:
            p = re.search("^.+S\d+", pathAndFilename, flags=re.IGNORECASE)
            if p:
                body = p.group(0)
        if filetype == 2:
            p = re.search("^.+E\d+", pathAndFilename, flags=re.IGNORECASE)
            if p:
                body = p.group(0)
        if body:
            body = body + '.' + ext
            os.rename(pathAndFilename, body)
        else:
            print("Something went wrong")
            exit(-7)


main()

import glob
import os
import sys
import re


# Silicon Valley E01 S02 2015 BDRip 1080p Кубик в кубе Amedia.mkv'

def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename, os.path.join(dir, titlePattern % title + ext))


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
    del s_reg, ep_reg, ext_reg
    return found_ep, found_s, ext


def defal():
    filename = sys.argv[1]
    direct = sys.argv[2]
    find_needed_parts(filename)

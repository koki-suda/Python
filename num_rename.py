# -*- coding: utf-8 -*-
import glob, os
directory = '/Users/user1/Documents/WIP/test/'
files = glob.glob(directory + "*.png")
i = 1
for old_name in files:
    num = "{0:02d}".format(i)
    new_name = num + ".png"
    new_print = directory + new_name
    os.rename(old_name, new_print)
    print(old_name + "→" + new_name)
    i += 1
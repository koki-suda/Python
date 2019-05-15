# -*- coding: utf-8 -*-
import os, sys
directory = '/Users/user1/Documents/ドキュメント/name'
files = os.listdir(directory)
for file in files:
    old_name = os.path.join(directory, file)
    rep = file.replace('_', '')
    new_name = os.path.join(directory, rep)
    os.rename(old_name, new_name)
    print(old_name + "→" + new_name)
#!/usr/bin/python3.6
# coding=utf-8

"""
Ova skripta prima stazu do arhive i zaporku za dešifriranje arhive.
Zaporka arihve u projektu je 'sifra'.
"""

import zipfile
from logging import warning
from sys import argv

if len(argv) < 3 or len(argv) > 4:
    print("Usage: zipfile-extract.py <path-to-archive> <path-to-extracted-archive> <archive-password>")
    exit(0)

path = "."
pwd = ""
if len(argv) == 4:
    path += "/" + argv[2]
    pwd = argv[3]
else:
    pwd = argv[2]

zFile = zipfile.ZipFile("./" + argv[1])
try:
    zFile.extractall(path=path, pwd=pwd.encode())
    print("[+]Files successfully extracted to '{0}'...".format(path))
except Exception as e:
    warning("[-]Wrong password for archive: {0}".format(argv[1]))

#!/usr/bin/python3.6
# coding = utf-8

import zipfile
from argparse import ArgumentParser
from os import path
from threading import Thread


def extract_file(z_file, password, ex_path):
    try:
        z_file.extractall(pwd=password.encode(), path=ex_path)
        print("[+]Password found: {0}".format(password))
    except RuntimeError:
        pass


# ovako izgleda single-thread probijanje
# def main():
#     if argv != 3:
#         print("Usage: zipfile-cracker.py <path-to-archive> <password-list>")
#         exit(0)
#     z_file = zipfile.ZipFile(path.join(".", argv[1]))
#     print("[*]Attacking zip archive {0}...".format(argv[1]))
#     for pwd in open(argv[2], 'r').readlines():
#         pwd = extract_file(z_file, pwd.strip())
#
#         if pwd:
#             print("[+]Password found: {0}".format(pwd))
#             exit(0)

def main():
    parser = ArgumentParser('Jednostavna skripta koja izvodi napad riječnikom na predanu zip arhivu.')
    parser.add_argument('archive_path', help='path to encrypted zip archive')
    parser.add_argument('dictionary', help='path to custom dictionary')
    parser.add_argument('-d', '--destination', dest='ex_path', help='path to extracted files', default='.')
    args = parser.parse_args()

    z_file = zipfile.ZipFile(path.join(".", args.archive_path))
    print("[*]Attacking zip archive {0}...".format(args.archive_path))
    for pwd in open(args.dictionary, 'r').readlines():
        ex_path = args.ex_path
        if ex_path == '.':
            ex_path = path.join('.', z_file.filename + '-extracted')
        Thread(target=extract_file, args=(z_file, pwd.strip('\n'), ex_path)).start()
    print("[-]Password not found, use a different word-list, or try again...")


if __name__ == '__main__':
    main()

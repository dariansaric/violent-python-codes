#!/usr/bin/python3.6
# coding=utf-8


import crypt
import hashlib
# import blowfish
from sys import argv

"""
Ova skripta služi za probijanje hasheva iz etc/shadow datoteke
"""

"""Ova funkcija prima hash-vrijednost i pomoću funkcije crypt šifrira zaporku
iz riječnika i uspoređuje s primljenom hashiranom zaporkom
"""


def test_pass(crypt_pass):
    salt = crypt_pass[0:2]
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        word = word.split('\n')
        crypt_word = crypt.crypt(word, salt)
        if crypt_word == crypt_pass:
            print("[+]Found Password: {0}\n".format(word))
            return
    print("[-]Password not found.\n")
    return


"""funkcija prima parametre pohranjene zaporke iz UNIX datoteke '/etc/shadow'"""


def test_shadow_pass(digest_id, salt, crypt_pass, wordlist):
    # todo: dodati u mapu blowfish
    hash_algorithms = {"1": "md5", "5": "sha256", "6": "sha512"}
    unimplemented_algorithm_ids = ["2a", "2y"]
    if digest_id in unimplemented_algorithm_ids:
        print("[-]Unimplemented algorithm id provided: {0}".format(digest_id))
        return

    for w in open(wordlist, 'r').readlines():
        w = w.strip()
        digest = hashlib.new(hash_algorithms[digest_id])
        digest.update(w)
        digest.update(salt)
        if crypt_pass == digest.hexdigest:
            print("[+]Password found: {0}".format(w))
            return

    print("[-]Password not found...")
    return


"""main funkcija"""


def main():
    if len(argv) != 3:
        print("[-]Usage: python3.6 <shadow-file> <dictionary-file>")
        exit(0)

    pass_file = (open(argv[2], 'r'))
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip(' ')
            print("[*]Cracking Password For: {0}".format(user))
            test_pass(crypt_pass)


if __name__ == "__main__":
    main()

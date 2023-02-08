#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding='utf-8') as name_files:
        print(name_files.read(),end="")
        name_files.close()

#!/usr/bin/python3
import marshal
import dis

def main():
    with open("hidden_4.pyc", "rb") as f:
        code = marshal.load(f)
    dis.dis(code)

if __name__ == "__main__":
    main()

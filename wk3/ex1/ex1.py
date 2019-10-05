#!/usr/bin/env python

from nornir import InitNornir

def main():
    nr = InitNornir()
    print(nr.inventory.hosts["arista3"].items())
    print(nr.inventory.hosts["arista3"].data)

if __name__ == "__main__":
    main()


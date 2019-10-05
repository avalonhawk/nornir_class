#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    nr = nr.filter(F(groups__contains="sea") | F(groups__contains="sfo"))
    print(nr.inventory.hosts)

if __name__ == "__main__":
    main()

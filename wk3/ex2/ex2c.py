#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    sfo = nr.filter(F(groups__contains="sfo"))
    print(sfo.inventory.hosts)

if __name__ == "__main__":
    main()

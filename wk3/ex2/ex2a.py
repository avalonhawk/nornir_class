#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    arista = nr.filter(name="arista1")
    print(arista.inventory.hosts)

if __name__ == "__main__":
    main()

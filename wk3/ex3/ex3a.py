#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    agg = nr.filter(F(role="AGG"))
    print(agg.inventory.hosts)

if __name__ == "__main__":
    main()

#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    wan = nr.filter(F(role="WAN")).filter(F(port=22))
    print(wan.inventory.hosts)

if __name__ == "__main__":
    main()

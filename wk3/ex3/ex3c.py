#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F

def main():
    nr = InitNornir()
    wan_wlan = nr.filter(F(role="WAN") & F(site_details__wifi_password__contains="racecar"))
    print(wan_wlan.inventory.hosts)

if __name__ == "__main__":
    main()

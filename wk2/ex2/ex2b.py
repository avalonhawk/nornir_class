#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
# import ipdb

def main():
    nr = InitNornir(config_file="config.yaml")
    filt = F(groups__contains="ios")
    nr = nr.filter(filt)
    my_results = nr.run(task=netmiko_send_command, command_string="show run | inc hostname")
    print()
    print(type(my_results))
    print(my_results.keys())
    print(my_results.items())
    print(my_results.values())

if __name__ == "__main__":
    main()

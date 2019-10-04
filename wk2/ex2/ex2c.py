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
    host_results=my_results["cisco3"]
    print()
    print(f"host_results is of type: {type(host_results)}")
    print(f"Zeroith element in host_results is: {repr(host_results[0])}")
    print(f"Zeroith element in host_results is: {host_results[0]}")
    print(f"Is host_results interable? {host_results.__iter__}") 

if __name__ == "__main__":
    main()

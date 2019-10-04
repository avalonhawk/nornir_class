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
    task_results=host_results[0]
    print()
    print(task_results.host)
    print(task_results.name)
    print(task_results.result)
    print(task_results.failed)

if __name__ == "__main__":
    main()

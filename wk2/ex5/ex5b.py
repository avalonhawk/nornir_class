#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F
import ipdb

def main():
    nr = InitNornir(config_file="config.yaml")
    ios_filt = F(groups__contains="ios")
    nr = nr.filter(ios_filt)
    nr.inventory.hosts['cisco3'].password = "notarealpassword"

    task = nr.run(task=netmiko_send_command, command_string="show ip interface brief")

    print_result(task)
    print("-" * 50)
    print(f"Failed Hosts shwon in task object: {task.failed_hosts}")
    print(f"Failed Hosts shown in nr object: {nr.data.failed_hosts}")
    print("-" * 50)

if __name__ == "__main__":
    main()

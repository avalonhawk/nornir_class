#!/usr/bin/env python

import os
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
    print(f"Task failed hosts: {task.failed_hosts}")
    print(f"Global failed hosts: {nr.data.failed_hosts}")
    print("-" * 50)

    print(f"Checking connection state on {task.failed_hosts}: {nr.inventory.hosts['cisco3'].connections}")
    try:
        nr.inventory.hosts["cisco3"].close_connections()
    except ValueError:
        pass

    print(f"Reseting password for host {task.failed_hosts}")
    nr.inventory.hosts["cisco3"].password = os.environ["NORNIR_PASSWORD"]

    print(f"Re-running task on {task.failed_hosts}")
    task = nr.run(task=netmiko_send_command, on_good=False, on_failed=True, command_string="show ip interface brief")

    print_result(task)
    print("-" * 50)
    print("Check and see if any hosts failed this time")
    print(f"Task failed hosts: {task.failed_hosts}")
    print(f"Global failed hosts: {nr.data.failed_hosts}")
    print("-" * 50)
    print("Recovering failed host")
    nr.data.recover_host("cisco3")
    print("Re-checking global failed object value...")
    print(f"Failed hosts: {nr.data.failed_hosts}")
    print("-" * 50)

if __name__ == "__main__":
    main()

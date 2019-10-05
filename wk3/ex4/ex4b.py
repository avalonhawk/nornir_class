#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from pprint import pprint

def main():
    nr = InitNornir(config_file="config.yaml")
    eos = nr.filter(F(groups__contains="eos"))
    results = eos.run(
        task=netmiko_send_command,
        command_string="show interface status",
        use_textfsm=True
    )
    print()
    for host in results:
        print("-" * 80)
        print(host)
        pprint(results[host].result)
        print("-" * 80)

if __name__ == "__main__":
    main()

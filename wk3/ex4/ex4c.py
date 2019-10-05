#!/usr/bin/env python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from pprint import pprint
import ipdb

def main():
    nr = InitNornir(config_file="config.yaml")
    eos = nr.filter(F(groups__contains="eos"))
    results = eos.run(
        task=netmiko_send_command,
        command_string="show interface status",
        use_textfsm=True
    )
    print()
    # create blank dictionary
    agg_data = {}
    # iterate through results items on two keys
    for host, multi_result in results.items():
        # add host key to = blank dictionary
        agg_data[host] = {}
        # unpack the result list item into a seperate var
        task_result = multi_result[0]
        # now iterate over the result dictionary
        for int_dict in task_result.result:
            # set the int_name key value - used later
            int_name = int_dict["port"]
            # create an empty inner dictionary
            inner_dict = {}
            # now create the inner key:value pairs
            inner_dict["status"] = int_dict["status"]
            inner_dict["vlan"] = int_dict["vlan"]
            # finally, set the int_name value to the inner dictonary
            agg_data[host][int_name] = inner_dict
    print("-" * 80)
    pprint(agg_data)

if __name__ == "__main__":
    main()

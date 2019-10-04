#!/usr/bin/env python

import os
from pprint import pprint
from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.core.filter import F

DEFAULT_GATEWAY = os.environ.get("EOS_GATEWAY", "10.220.88.1")

def main():
    nr = InitNornir(config_file="config.yaml")
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    nr = nr.filter(ios_filt | eos_filt)

    results = nr.run(task=napalm_get, getters="arp_table")

    parsed_results = []
    for host, multi_result in results.items():
        output = multi_result[0].result
        gateway_data = ""
        for items in output["arp_table"]:
            if items["ip"] == DEFAULT_GATEWAY:
                gateway_data = items
                break
        print(f"Host: {host}, Gateway: {gateway_data}")

if __name__ == "__main__":
    main()

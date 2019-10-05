#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.core.filter import F
from pprint import pprint

def main():
    nr = InitNornir(config_file="config.yaml")
    nxos = nr.filter(F(platform="nxos"))
    results = nxos.run(
        task = napalm_get,
        getters = "config",
        getters_options = {"config": {"retrieve": "running"}}
    )
    for host, multi in results.items():
        print("=" * 80)
        print(f"Device {host}")
        pprint(multi[0].result)


if __name__ == "__main__":
    main()

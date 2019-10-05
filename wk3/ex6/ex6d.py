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
        getters = ["config", "facts"],
        getters_options = {"config": {"retrieve": "all"}}
    )
    agg_data = {}
    for host, multi_result in results.items():
        agg_data[host] = {}
        host_results = multi_result[0]

        configs = host_results.result["config"]
        start_config = configs["startup"].split("\n")[4:]
        run_config = configs["running"].split("\n")[4:]

        facts = host_results.result["facts"]

        inner_dict = {}
        if start_config == run_config:
            inner_dict["start_running_match"] = True
        else:
            inner_dict["start_running_match"] = False
        inner_dict["model"] = facts["model"]
        inner_dict["uptime"] = facts["uptime"]
        inner_dict["vendor"] = facts["vendor"]
        agg_data[host] = inner_dict
    print()
    pprint(agg_data)

if __name__ == "__main__":
    main()

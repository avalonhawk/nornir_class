#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir(config_file="config.yaml", core={"num_workers":15})

print(f"Number of workers is: {nr.config.core.num_workers}")


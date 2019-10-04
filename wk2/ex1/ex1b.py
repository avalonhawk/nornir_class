#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

print(f"Number of workers is: {nr.config.core.num_workers}")


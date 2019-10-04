#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir()

print(f"Number of workers is: {nr.config.core.num_workers}")


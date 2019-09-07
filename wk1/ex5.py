#!/usr/bin/env python
import time
from random import random
from nornir import InitNornir

def my_task(task):
    host = task.host
    time.sleep(random())
    print()
    print(host.hostname)
    print(f"DNS1: {host['dns1']}")
    print(f"DNS2: {host['dns2']}")
    print('-' * 25)
    print()

def main():
    nr = InitNornir()
    nr.run(task=my_task)

if __name__ == "__main__":
    main()

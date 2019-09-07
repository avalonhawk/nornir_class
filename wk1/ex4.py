#!/usr/bin/env python
import time
from random import random
from nornir import InitNornir

def my_task(task):
    time.sleep(random())
    print()
    print(task.host.hostname)
    print('-' * 80)
    print("yay a task ran")
    print()

def main():
    nr = InitNornir()
    nr.run(task=my_task)

if __name__ == "__main__":
    main()

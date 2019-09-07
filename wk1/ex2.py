#!/usr/bin/env python

from nornir import InitNornir

nr = InitNornir()

for host_name, host_obj in nr.inventory.hosts.items():
    print()
    print(f'Host: {host_name}')
    print('-' * 25)
    print(f'Hostname: {host_obj.hostname}')
    print(f'Groups: {host_obj.groups}')
    print(f'Platform: {host_obj.platform}')
    print(f'Username: {host_obj.username}')
    print(f'Password: {host_obj.password}')
    print(f'Port: {host_obj.port}')
    print()


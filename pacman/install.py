#!/usr/bin/env python3
"""
Author: Name
Date  : 05/24/23
Desc  : Description
"""


import getpass
import subprocess
import sys


def packages_get():
    packages = ''
    with open('_packages.ini', 'r') as file:
        for line in file:
            if not line.startswith('[') and not line.startswith('#') and line.strip() != '':
                packages += f'{line.rstrip()} '
    return packages

def packages_install(packages: str):
    cmd = f'sudo pacman -S --noconfirm {packages}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print('[-] Install', err)
        sys.exit(1)

def group_add(user: str):
    groups = 'wireshark'
    cmd = f'sudo usermod -aG {groups} {user}'
    try:
        subprocess.run(cmd, shell=True, check=True)
    except Exception as err:
        print('[-] Install', err)
        sys.exit(1)


if __name__ == "__main__":
    packages = packages_get()
    packages_install(packages)

    user = getpass.getuser()
    group_add(user)

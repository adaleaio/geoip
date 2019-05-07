#!/usr/bin/env python3

import requests
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-i','--ip',help="IP Address", required=True)

args = argparser.parse_args()

ip = args.ip


def main():
  print(ip)


if '__main__' in __name__:
    main()


#!/usr/bin/env python3

import argparse
import geoip2.database
import re

ip = '8.8.8.8'
ipfile = ''

argparser = argparse.ArgumentParser()
argparser.add_argument('-i','--ip',help="IP Address", required=False)
argparser.add_argument('-f','--file',help="IP Address File", required=False)
args = argparser.parse_args()

if args.ip:
    ip = args.ip
if args.file:
    ipfile = args.file


reader = geoip2.database.Reader('./GeoLite2-City_20190423/GeoLite2-City.mmdb')

if '__main__' in __name__:
    if ip:
        ipinfo = reader.city(ip)
        print("{} - {},{}".format(ip,ipinfo.city.name,ipinfo.subdivisions[0].iso_code))


    if ipfile != ''  :
        with open(ipfile,'r') as ipfile:
            for ip in ipfile:
               ip = re.sub('\n','',ip)
               try:
                   ipinfo = reader.city(ip)
                   if ipinfo.city.name and ipinfo.subdivisions[0].iso_code:
                       print("{} - {},{}".format(ip,ipinfo.city.name,ipinfo.subdivisions[0].iso_code)) 
                   elif ipinfo.subdivisions[0].iso_code:
                       print("{} - {}".format(ip,ipinfo.subdivisions[0].iso_code))
               except:
                   print("{}".format(ip))
#!/usr/bin/env python
#
# CWCreator - Create a simple, secure wireless network with an expiration time specified in days.
#
#    usage: cwcreator.py [-h] [--token TOKEN] [--site_id SITE_ID] [--ssid SSID] [--psk PSK] [--vlan VLAN] [--duration DURATION]
#
#    optional arguments:
#      -h, --help           show this help message and exit
#      --token TOKEN        Mist API token
#      --site_id SITE_ID    Mist site ID
#      --ssid SSID          The wireless network name
#      --psk PSK            PSK for the wireless network
#      --vlan VLAN          VLAN ID for the wireless network (default: VLAN 1)
#      --duration DURATION  Number of days to keep the wireless network online (default: 7 days)
#

from cwc import *
from datetime import datetime, timedelta


if __name__ == '__main__':
    args = parse_cli()
    new_wlan = create_wlan(**args)
    created_date = datetime.fromtimestamp(new_wlan['created_time'])
    destroy_date = created_date + timedelta(days=args['duration'])
    log.info(f"Created WLAN at {created_date.strftime(DATEFMT)}")
    log.info(f"WLAN to be destroyed at approx {destroy_date.strftime(DATEFMT)}")
    log.info(f"WLAN ID: {new_wlan['id']}")

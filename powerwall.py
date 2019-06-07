#!/usr/bin/env python3

"""
powerwall reporting utility
"""

import requests
import json
import smtplib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# set your powerwall ip here
powerwall_ip="192.168.1.30"

pwall_stats_url="https://{}/api/meters/aggregates".format(powerwall_ip)
pwall_stats_request=requests.get(pwall_stats_url, verify=False)
pwall_stats_data=json.loads(pwall_stats_request.text)

pwall_charge_url="https://{}/api/system_status/soe".format(powerwall_ip)
pwall_charge_request=requests.get(pwall_charge_url, verify=False)
pwall_charge_data=json.loads(pwall_charge_request.text)


# uncommend this line to see all available data:
# print(json.dumps(pwall_stats_data, sort_keys=True, indent=4))

current_solar_draw=((pwall_stats_data)["solar"]["instant_power"]/1000)
current_home_draw=((pwall_stats_data)["load"]["instant_power"]/1000)
current_grid_draw=((pwall_stats_data)["site"]["instant_power"]/1000)
current_powerwall_draw=((pwall_stats_data)["battery"]["instant_power"]/1000)
current_powerwall_charge=((pwall_charge_data)["percentage"])

print("\nCurrently Producing from Solar: {} kW".format(round(current_solar_draw,2)))
print("Currently pulling from grid: {} kW".format(round(current_grid_draw,2)))
print("Currently pulling from powerwall: {} kW".format(round(current_powerwall_draw,2)))
print("Currently powerwall charge: {} % \n".format(round(current_powerwall_charge,2)))
print("Current Home Load: {} kW\n".format(round(current_home_draw,2)))




# This is a sample Python script to demonstrate pagination with and without the Meraki SDK

import meraki
import requests
import json
import csv

API_KEY = ""


def add_to_csv(itemlistFull):
    """
    This function accepts a list and dumps it to a csv
    :param itemlistFull: list
    :return:
    """
    itemlistSelection: list
    itemlistSelection = [{'name': line['name'], 'serial': line['serial'], 'productType': line['productType'],
                 'model': line['model']} for line in itemlistFull]
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'serial', 'productType', 'model']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in itemlistSelection:
            writer.writerow(row)
    return


def get_devices_sdk(organization_id):
    """
    gets a list of devices from an org via the meraki sdk
    :return: devices -> list
    """
    devices = dashboard.organizations.getOrganizationDevices(
        organization_id, total_pages='all')
    return devices


def get_devices_requests(organization_id):
    """
    gets a list of devices from an org via the requests library
    :return: devices -> list
    """
    devices: list
    url = f"https://api.meraki.com/api/v1/organizations/{organization_id}/devices"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": API_KEY
    }

    params = {'perPage': '3'}

    response = requests.request('GET', url, headers=headers, params=params, data=payload)
    # print(response.json())
    devices = response.json()

    while 'next' in response.links:
        print(response.links['next']['url'])
        response = requests.get(response.links['next']['url'], headers=headers, params=params, data=payload)
        for line in response.json():
            devices.append(line)

    return devices


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dashboard = meraki.DashboardAPI(API_KEY)
    # print(json.dumps(dashboard.organizations.getOrganizations(), indent=4))
    organization_id = "940024"
    # print(json.dumps(get_devices_sdk(organization_id), indent=4))
    # add_to_csv(get_devices_sdk(organization_id))
    # print(get_devices_requests(organization_id))
    # add_to_csv(get_devices_requests(organization_id))


# This is a sample Python script to demonstrate pagination with and without the Meraki SDK

"""
Start by getting a list of orgs your key has access to.
Then use the SDK to get all of the organization devices at once.
Finally, try that with the requests library
"""

import meraki
import csv


def add_to_csv(itemlist):
    """
    This function accepts a list and dumps it to a csv
    :param itemlist: list
    :return:
    """
    return


def get_devices_sdk():
    """
    gets a list of devices from an org via the meraki sdk
    :return: devices -> list
    """
    devices = []
    return devices


def get_devices_requests():
    """
    gets a list of devices from an org via the requests library
    :return: devices -> list
    """
    devices = []
    return devices


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:50:52 2017

@author: jbs-
"""

import requests
import json

def build_output(tracking_number):

    data = requests.post('https://www.fedex.com/trackingCal/track', data={
        'data': json.dumps({
            'TrackPackagesRequest': {
                'appType': 'wtrk',
                'uniqueKey': '',
                'processingParameters': {
                    'anonymousTransaction': True,
                    'clientId': 'WTRK',
                    'returnDetailedErrors': True,
                    'returnLocalizedDateTime': False
                },
                'trackingInfoList': [{
                    'trackNumberInfo': {
                        'trackingNumber': tracking_number,
                        'trackingQualifier': '',
                        'trackingCarrier': ''
                    }
                }]
            }
        }),
        'action': 'trackpackages',
        'locale': 'en_US',
        'format': 'json',
        'version': 99
    }).json()

    return data

# finds last status info

statusWithDetails = 'statusWithDetails'

def track(tracking_number):

    data = build_output(tracking_number)
     #narrowing down dictionary and lists to objects needed
    for key, value in data.items():
        narrow = value 
    #narrow more into packageList list
    for key, value in narrow.items():
        if key == 'packageList':
            narrow = value
    # narrow to last status
    for x, y in narrow[0].items():
        if x == statusWithDetails:
            last_status = y
            exists = True
    return last_status, exists


def print_results(tracking_number):
    printing_last_status = track(tracking_number)
    print(printing_last_status[0])

print_results(723601323311)
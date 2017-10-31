#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

class Fee:

    def __init__(self):
        self.url = 'https://bitcoinfees.earn.com/api/v1/fees/'
        self.url_for_recommended = self.url + 'recommended'

    # recommended fees
    ## fee types: 'fastestFee', 'halfHourFee', 'hourFee'
    def fastest_fee(self):
        result = requests.get(self.url_for_recommended).json()
        return result['fastestFee']

    def half_hour_fee(self):
        result = requests.get(self.url_for_recommended).json()
        return result['halfHourFee']

    def hour_fee(self):
        result = requests.get(self.url_for_recommended).json()
        return result['hourFee']


    # Transaction Fees Summary

    # private methods
    # def __get(self, fee_type):
    #     response = requests.get(self.url).json()
    #     return response[fee_type]

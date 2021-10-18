#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import ParamSpec
import requests
import json

class IP():

    def __init__(self,ipAddress,subnet=None):
        self.ip = ipAddress
        self.subnet = subnet

    def calıs(self):
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1
    
    def whois(self):

        # Sending an API request
        response = requests.get("http://ipwhois.app/json/"+self.ip)
        ipgeolocation = json.loads(response.content.decode("utf-8"))

        # Country code output, field "country_code"
        #print(ipgeolocation)
        print(json.dumps(ipgeolocation, indent=4, sort_keys=True))
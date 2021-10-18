#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.ip import IP

print("""

  _________.___.____     _______________  ___.___        ___________.___ 
 /   _____/|   |    |    \_   _____/\   \/  /|   |       \__    ___/|   |
 \_____  \ |   |    |     |    __)_  \     / |   |  ______ |    |   |   |
 /        \|   |    |___  |        \ /     \ |   | /_____/ |    |   |   |
/_______  /|___|_______ \/_______  //___/\  \|___|         |____|   |___|
        \/             \/        \/       \_/                            

#########################################################################
Silexi-TI is Passive Information Gathering Tool.
#########################################################################

Options:
1- IP
2- Domain
3- URL
4- Hash
If you want to Auto Detect press the "Enter" key.

""")
userInput = input("Please select an option:")
if userInput == "1":
    indicator = IP("142.250.72.110")
    indicator.whois()
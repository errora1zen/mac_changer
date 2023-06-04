#!/usr/bin/env python

import subprocess as sp
import optparse as op

#For getting the arguments
def arguments():
    parser = op.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not options.mac:
         parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

#Function to change the MAC address
def mac_change(interface,mac):
    print("[+] Changing MAC address for " + interface + " to " + mac)
    sp.call(["sudo","ifconfig", interface, "down"])
    sp.call(["sudo","ifconfig", interface, "hw", "ether", mac])
    sp.call(["sudo", "ifconfig", interface, "up"])

#Function calls
options = arguments()
mac_change(options.interface,options.mac)


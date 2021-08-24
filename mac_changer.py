#!/usr/bin/env python

import subprocess
import optparse
import re

def get_agruments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="NEW mac address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] please specify a new mac, use --help for more info.")
    return options

def change_mac(interface , new_mac):
    print("[+] Changing MAC address for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface,  "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] could not read mac address")


options =get_agruments()

current_mac = get_current_mac(options.interface)
print("current MAC " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac :
    print("[+] MAC address was successfully change to " + current_mac )
else:
    print("[+] MAC address did not get changed")


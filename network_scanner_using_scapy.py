#!/usr/bin/env python

import scapy.all as scapy
import argparse


def get_agruments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="this is where you define the current ip range so that we can target over it")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout =1 , verbose = False )[0]
    client_list =[]
    for element in answer_list:
        client_dict = {"ip":element[1].prsc, "mac":element[1].hwsrc }
        clients_list.append(client_dict)
        print(element[1].prsc + "\t\t" + element[1].hwsrc)
    return clients_list

def print_result(result_list):
    print("IP \t\t\t MAC Address\n ------------------")
    for client in result_list:
        print(client["ip"]+ "\t\t"+ client["mac"])



scanres = get_agruments()
scan_result = scan(scanres.target)
print_result(scan_result)

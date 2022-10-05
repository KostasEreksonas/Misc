#!/usr/bin/env python3

from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
import os

# Data for encding
protocol_type = np.asarray([['tcp'], ['udp'], ['icmp']])

service = np.asarray([['aol'], ['auth'], ['bgp'], ['courier'], ['csnet_ns'], ['ctf'], ['daytime'], ['discard'], ['domain'], ['domain_u'], ['echo'], ['eco_i'], ['ecr_i'], ['efs'], ['exec'], ['finger'], ['ftp'], ['ftp_data'], ['gopher'], ['harvest'], ['hostnames'], ['http'], ['http_2784'], ['http_443'], ['http_8001'], ['imap4'], ['IRC'], ['iso_tsap'], ['klogin'], ['kshell'], ['ldap'], ['link'], ['login'], ['mtp'], ['name'], ['netbios_dgm'], ['netbios_ns'], ['netbios_ssn'], ['netstat'], ['nnsp'], ['nntp'], ['ntp_u'], ['other'], ['pm_dump'], ['pop_2'], ['pop_3'], ['printer'], ['private'], ['red_i'], ['remote_job'], ['rje'], ['shell'], ['smtp'], ['sql_net'], ['ssh'], ['sunrpc'], ['supdup'], ['systat'], ['telnet'], ['tftp_u'], ['tim_i'], ['time'], ['urh_i'], ['urp_i'], ['uucp'], ['uucp_path'], ['vmnet'], ['whois'], ['X11'], ['Z39_50']])

flag = np.asarray([['OTH'], ['REJ'], ['RSTO'], ['RSTOS0'], ['RSTR'], ['S0'], ['S1'], ['S2'], ['S3'], ['SF'], ['SH']])

logged_in = np.asarray([['0'], ['1']])

is_host_login = np.asarray([['0'], ['1']])

is_guest_login = np.asarray([['0'], ['1']])

classs = np.asarray([['normal'], ['anomaly']])

# Dictionary that contains mapping of various attacks to the four main categories
attack_dict = {
    'normal': 'normal',

    'back': 'DoS',
    'land': 'DoS',
    'neptune': 'DoS',
    'pod': 'DoS',
    'smurf': 'DoS',
    'teardrop': 'DoS',
    'mailbomb': 'DoS',
    'apache2': 'DoS',
    'processtable': 'DoS',
    'udpstorm': 'DoS',

    'ipsweep': 'Probe',
    'nmap': 'Probe',
    'portsweep': 'Probe',
    'satan': 'Probe',
    'mscan': 'Probe',
    'saint': 'Probe',

    'ftp_write': 'R2L',
    'guess_passwd': 'R2L',
    'imap': 'R2L',
    'multihop': 'R2L',
    'phf': 'R2L',
    'spy': 'R2L',
    'warezclient': 'R2L',
    'warezmaster': 'R2L',
    'sendmail': 'R2L',
    'named': 'R2L',
    'snmpgetattack': 'R2L',
    'snmpguess': 'R2L',
    'xlock': 'R2L',
    'xsnoop': 'R2L',
    'worm': 'R2L',

    'buffer_overflow': 'U2R',
    'loadmodule': 'U2R',
    'perl': 'U2R',
    'rootkit': 'U2R',
    'httptunnel': 'U2R',
    'ps': 'U2R',
    'sqlattack': 'U2R',
    'xterm': 'U2R'
}

# Define One Hot Encoding
encoder = OneHotEncoder(sparse=False)

# Data Transformation
print("[+] Categorical data transformation")
print("[+] Protocols")
print("---------------------------------------------------")
print(protocol_type)
protocol_type_encoded = encoder.fit_transform(protocol_type)
print(protocol_type_encoded)
print("---------------------------------------------------")
print("[+] Services")
print("---------------------------------------------------")
print(service)
service_encoded = encoder.fit_transform(service)
print(service_encoded)
print("---------------------------------------------------")
print("[+] Flags")
print("---------------------------------------------------")
print(flag)
flag_encoded = encoder.fit_transform(flag)
print(flag_encoded)
print("---------------------------------------------------")
print("[+] Logged in")
print("---------------------------------------------------")
print(logged_in)
logged_in_encoded = encoder.fit_transform(logged_in)
print(logged_in_encoded)
print("---------------------------------------------------")
print("[+] Is host login")
print("---------------------------------------------------")
print(is_host_login)
is_host_login_encoded = encoder.fit_transform(is_host_login)
print(is_host_login_encoded)
print("---------------------------------------------------")
print("[+] Is guest login")
print("---------------------------------------------------")
print(is_guest_login)
is_guest_login_encoded = encoder.fit_transform(is_guest_login)
print(is_guest_login_encoded)
print("---------------------------------------------------")
print("[+] Class")
print("---------------------------------------------------")
print(classs)
class_encoded = encoder.fit_transform(classs)
print(class_encoded)

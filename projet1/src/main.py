# -*- coding: utf-8 -*-
from MonPackage.random import random_domain, random_ip, random_external_ip
from traceback import print_exc
import re

# try:
#     with open("listing.txt", "w") as file:
#         file.write("Hello\n")
# except FileNotFoundError as e:
#     print("Error")
#     print_exc()
# except:
#     print("Any Error")
#     print_exc()
    
# help(random_domain)
    
# 192.168.1.1 local.mondomain.com
# 192.168.1.1 local.mondomain.com
# 192.168.1.1 local.mondomain.com
# 192.168.1.1 local.mondomain.com

# Générer le listing domain ip interne
with open("listing.txt", "w") as f:
    for i in range(10):
        f.write(f"{random_domain()} {random_ip()}\n")
        
        
# Générer le listing ip externe ip interne
with open("listing.txt", "r") as file_input:
    content = file_input.read()
    ip_list = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", content)
    external_ip_list = [random_external_ip() for i in range(10)]
    with open("lookup.txt", "w") as f:
        for i in range(10):
            f.write(f"{ip_list[i]} {external_ip_list[i]}\n")
        
# Afficher les paires domain / ip externe
with open("listing.txt", "r") as file_input:
    content = file_input.read()
    couple_domain_ip = re.findall("(.*) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", content)
    print(couple_domain_ip)
with open("lookup.txt", "r") as file_input:
    content = file_input.read()
    couple_intern_extern = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\n", content)
    print(couple_intern_extern)

for domain, ip in couple_domain_ip:
    externe = [couple[1] for couple in couple_intern_extern if couple[0] == ip][0]
    print(f"le domaine : {domain} est associé à {externe}")
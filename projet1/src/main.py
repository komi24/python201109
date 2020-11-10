# -*- coding: utf-8 -*-
from MonPackage.random import random_domain, random_ip
from traceback import print_exc


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

with open("listing.txt", "w") as f:
    for i in range(10):
        f.write(f"{random_domain()} {random_ip()}\n")
        
        
        
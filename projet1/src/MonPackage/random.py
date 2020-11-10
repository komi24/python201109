# -*- coding: utf-8 -*-
from random import randint as rd

SUBDOMAIN_SET = [
    "local",
    "dev",
    "api",
    "mail",
    "app",
]

DOMAIN_SET = [
    "mondomain.com",
    "mydomain.com",
    "mondomain.fr",
]

def random_ip():
    """
    192.168.xxx.xxx
    """
    return f"192.168.{rd(0,255)}.{rd(0,255)}"

def random_external_ip():
    return f"182.244.12.{rd(0,255)}"
    

def random_domain():
    """
    

    Returns
    -------
    None.

    """
    subdomain = SUBDOMAIN_SET[rd(0,len(SUBDOMAIN_SET)-1)]
    domain = DOMAIN_SET[rd(0,len(DOMAIN_SET)-1)]
    return subdomain + "." + domain


if __name__ == "__main__":
    print(random_ip())
    print(random_domain())


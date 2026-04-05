import ipaddress
import math

def calculate_vlsm(base_network, subnets_req):
    base = ipaddress.IPv4Network(base_network, strict=False)
    sorted_subnets = sorted(subnets_req, key=lambda x: x['hosts'], reverse=True)

    total_required = 0
    for subnet in sorted_subnets:
        hosts = subnet['hosts']
        if hosts <= 0:
            print(f"Error: Invalid host count in subnet '{subnet['name']}'")
            return
        total_required += 2 ** math.ceil(math.log2(hosts + 2))

    if total_required > base.num_addresses:
        print("Error: Subnets do not fit within the base network")
        print(f"Base network capacity: {base.num_addresses} addresses")
        print(f"Total required addresses: {total_required}")
        return

    current_ip = base.network_address

    print(f"{'Subnet Name':<20} | {'Hosts':<6} | {'Network/CIDR':<22} | {'First Usable':<18} | {'Broadcast':<18} | {'Subnet Mask'}")
    print("-" * 115)

    for subnet in sorted_subnets:
        hosts = subnet['hosts']

        required_addresses = hosts + 2
        prefix_length = 32 - math.ceil(math.log2(required_addresses))

        network = ipaddress.IPv4Network(f"{current_ip}/{prefix_length}", strict=False)

        network_addr = str(network.network_address)
        first_usable = str(network.network_address + 1)
        broadcast = str(network.broadcast_address)
        netmask = str(network.netmask)

        print(f"{subnet['name']:<20} | {hosts:<6} | {network_addr + '/' + str(prefix_length):<22} | {first_usable:<18} | {broadcast:<18} | {netmask}")

        current_ip = network.broadcast_address + 1


base_network = "172.16.0.0/16"

requirements = [
    {"name": "ES-1 LAN", "hosts": 1035},
    {"name": "ES-2 LAN", "hosts": 2041},
    {"name": "WS-1 LAN", "hosts": 145},
    {"name": "WS-2 LAN", "hosts": 72},
]

calculate_vlsm(base_network, requirements)

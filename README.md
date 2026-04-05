VLSM Subnet Calculator

This Python script automates the process of Variable Length Subnet Mask (VLSM) calculation. Given a base IPv4 network and a list of required subnets with specific host capacities, it efficiently divides the address space.

Key Features:

Automatic Sorting: Sorts subnets from largest to smallest to ensure optimal address allocation.

Capacity Validation: Checks if the requested subnets fit within the base network before calculating.

Error Handling: Prevents calculations with invalid (zero or negative) host counts.

Clear Output: Generates a formatted table displaying the Subnet Name, Needed Hosts, Network Address/CIDR, First Usable IP, Broadcast Address, and Subnet Mask.

In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to --------------------------

1. Have the resources in the two regions contain the same virtual network (A, B) and enable peering (C, D).

2. Make sure that the values for the two virtual networks (A and B) are the same in both regions.

3. Ensure that the link between the two regions is a virtual network (A, B) in both regions.

======================

If the two regions are in different regions

1. Create two virtual networks in each region.

2. Enable peering between the two virtual networks.

3. Ensure that the link between the two regions is a virtual network (A, B) in both regions.

======================

If the region is the same region

1. Create one virtual network in each region.

2. Enable peering between the two virtual networks.

3. Ensure that the link between the two regions is a virtual network (A, B) in both regions.

======================

If the region is new or Azure Virtual Networks are not yet deployed in the region

1. Create one virtual network in each region.

2. Enable peering between the two virtual networks

3. Ensure that the link between the two regions is a virtual network (A, B) in both regions.

======================

Update: How to enable peering between two virtual networks of the
---------------

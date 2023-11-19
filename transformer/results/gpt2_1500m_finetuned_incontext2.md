In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to 
 * [Make sure that they have the same prefix so that all the traffic is sent through the same backbone gateway](../azure-networks/configure-virtual-network-peering.md).
* [Make sure that they're on the same subnet](../azure-networks/configure-virtual-network-peering.md#subnets-within-virtual-network). On the Azure portal, access the Azure Virtual Networks management console and select the local subnet in the **VirtualNetworkPeering Status** section.

**Important:** Make sure that the same prefix is used in both regions for all the virtual machines in the peered virtual networks to ensure that only one virtual network is ever down.

**Note:** Subnets used for peering are assumed to be on the same subnet, subnet mask, or subnets in the AS subnet table. If you use a subnet mask in the AS table, make sure to use the same subnet mask in the peered virtual networks.

## Requirements

* You need to be deployed on the same Azure subscription as the virtual network.
* Set up both networks in the same region to ensure that they have the same prefix so that all the traffic is sent through the same backbone gateway.

* Set up the VPN gateway on the same subnet as the virtual network and be sure that the gateway is configured as a link-local
---------------

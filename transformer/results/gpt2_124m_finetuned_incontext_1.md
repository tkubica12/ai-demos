In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  enable any userspace policy that allows virtual networks to access the same Azure user-defined routes.

For instance, you may wish to enable the following policy to send traffic to an Azure P2P virtual network that's closed:

• P2P* Virtual network: Receive traffic from any source in the link-free Azure network.


• P2P* Azure network: In a closed link-free Azure network, access to the Azure user-defined routes from the local interface.


In a closed links-free Azure network, userspace policy allows userspace to connect to the same Azure restpoints in two different regions. To learn how to set up this role, see [Setting up linked virtual networks](https://github.com/Azure/azure-virtual-network/blob/master/guide/virtual-network-network-manager/default-policy-user-defined-route-network).

## Efficient connectivity

To enable a user-defined PEering routing policy that enables peering, Azure Resource Manager enables your peering policy to send traffic to a single Azure Network using the following routes:

• Peering policy: Peering policy: |Peering| sends the traffic to the Azure Network.

• Peering policy: |Peering| sends the traffic to the Azure Network.

For example:

1) The peering policy states that a user-defined PEering
---------------

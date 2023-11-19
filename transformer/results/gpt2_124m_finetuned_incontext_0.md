In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  enable *Azure Virtual Networks** in the Azure Portal so that all user-defined routes in the peered virtual network are available.

For an example of a testnet and hub interface, see [Testnet and hub interface configuration](./portal-users/testnet-and-hub-interface.md).

In the Azure Portal, you can connect different virtual network peering into a single virtual network. Azure Virtual Networks access a single Azure portal via a gateway.
You don't need to configure a portal for peering between virtual networks. You can connect to a virtual network from the same portal via a gateway, or reuse a portal in a different portal. You can access a virtual network only by using the same portal across the virtual network.

In the same virtual network, you can access the portal directly from a gateway, or use a portal in a different portal.

## Readiness

The use case of peering in Azure Virtual Networks was primarily because a peering peering scenario was provided with a built-in Azure Resource Manager for your virtual network, so you could use it to communicate with distributed resources, directly or indirectly.

The Azure Resource Manager enables you to read resources in multiple virtual networks in Azure Virtual Networks, and examine them in your virtual network.

For more information about readiness, see [Readiness for virtual networks](../azure-resource-manager/management/readiness.md#read
---------------

Overriding: out_dir = azure_docs_finetuning_out
Overriding: num_samples = 1
Overriding: max_new_tokens = 300
Overriding: start = FILE:prompts/enhanced-1000.txt
number of parameters: 123.65M
No meta.pkl found, assuming GPT-2 encodings...
# Virtual network peering

Virtual network peering enables you to seamlessly connect two or more [Virtual Networks](virtual-networks-overview.md) in Azure. The virtual networks appear as one for connectivity purposes. The traffic between virtual machines in peered virtual networks uses the Microsoft backbone infrastructure. Like traffic between virtual machines in the same network, traffic is routed through Microsoft's *private* network only.

Azure supports the following types of peering:

* **Virtual network peering**: Connecting virtual networks within the same Azure region.

* **Global virtual network peering**: Connecting virtual networks across Azure regions.

The benefits of using virtual network peering, whether local or global, include:

* A low-latency, high-bandwidth connection between resources in different virtual networks.

* The ability for resources in one virtual network to communicate with resources in a different virtual network.

* The ability to transfer data between virtual networks across Azure subscriptions, Azure Active Directory tenants, deployment models, and Azure regions.

* The ability to peer virtual networks created through the Azure Resource Manager.

* The ability to peer a virtual network created through Resource Manager to one created through the classic deployment model. To learn more about Azure deployment models, see [Understand Azure deployment models](../azure-resource-manager/management/deployment-models.md?toc=%2fazure%2fvirtual-network%2ftoc.json).

* No downtime to resources in either virtual network when creating the peering, or after the peering is created.

Network traffic between peered virtual networks is private. Traffic between the virtual networks is kept on the Microsoft backbone network. No public Internet, gateways, or encryption is required in the communication between the virtual networks.

## Connectivity

For peered virtual networks, resources in either virtual network can directly connect with resources in the peered virtual network.

The network latency between virtual machines in peered virtual networks in the same region is the same as the latency within a single virtual network. The network throughput is based on the bandwidth that's allowed for the virtual machine, proportionate to its size. There isn't any extra restriction on bandwidth within the peering.

The traffic between virtual machines in peered virtual networks is routed directly through the Microsoft backbone infrastructure, not through a gateway or over the public Internet.

You can apply network security groups in either virtual network to block access to other virtual networks or subnets.
When you configure virtual network peering, either open or close the network security group rules between the virtual networks. If you open full connectivity between peered virtual networks, you can apply network security groups to block or deny specific access. Full connectivity is the default option. To learn more about network security groups, see [Security groups](./network-security-groups-overview.md).

## Service chaining

Service chaining enables you to direct traffic from one virtual network to a virtual appliance or gateway in a peered network through user-defined routes.

To enable service chaining, configure user-defined routes that point to virtual machines in peered virtual networks as the *next hop* IP address. User-defined routes could also point to virtual network gateways to enable service chaining.

You can deploy hub-and-spoke networks, where the hub virtual network hosts infrastructure components such as a network virtual appliance or VPN gateway. All the spoke virtual networks can then peer with the hub virtual network. Traffic flows through network virtual appliances or VPN gateways in the hub virtual network.

Virtual network peering enables the next hop in a user-defined route to be the IP address of a virtual machine in the peered virtual network, or a VPN gateway. You can't route between virtual networks with a user-defined route that specifies an Azure ExpressRoute gateway as the next hop type. To learn more about user-defined routes, see [User-defined routes overview](virtual-networks-udr-overview.md#user-defined). To learn how to create a hub and spoke network topology, see [Hub-spoke network topology in Azure](/azure/architecture/reference-architectures/hybrid-networking/hub-spoke?toc=%2fazure%2fvirtual-network%2ftoc.json).

-----------------------------------

In order to configure two Azure Virtual Networks in two different regions to communicate with each other you need to  enable any existing configuration rules that apply to the network for the  Azure Virtual Networks. 

The following  configurations enable a single virtual network peering to a virtual appliance or gateway in a peered virtual network that's configured to be the next hop in a user-defined route.

If you're using Azure Virtual Networks, you can use a local guest IP address to connect to the virtual appliance or gateway. On the Azure Marketplace, access to this IP address is restricted to Azure Active Directory.

If you're using Azure Virtual Networks, you can use a full-stack virtual network peering IP address to connect to an Azure Active Directory tenant.

The following  configurations allow access to the IP address of a virtual appliance, or a virtual network gateway.

If you're using Azure Virtual Networks, you can use the Guest IP range, however you need to use the AD-based ASV network web interface.

The following configuration allow access to the Hyper-V virtual network IP range.

The guest IP range is a single IP address that points to the Azure Virtual Network.

The IP range is distributed between virtual machines, virtual networks, and virtual appliance.

The IP range is managed by Azure Active Directory.

Each VM in the virtual network is assigned a guest IP address, which you can use to configure the zone membership.

The IP range on the guest IP address is managed through a role, which is a
---------------

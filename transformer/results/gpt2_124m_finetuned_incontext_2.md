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
